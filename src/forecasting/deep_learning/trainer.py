import torch
import os

class Trainer:

    @staticmethod
    def train(
        model,
        train_loader,
        validation_loader,
        optimizer,
        criterion,
        epochs=20,
        patience=5,
        checkpoint_name='model_best.pt'
    ):
        model.train()

        best_validation_loss = float('inf')
        epochs_without_improvement = 0

        checkpoint_dir = 'artifacts/models'

        os.makedirs(
            checkpoint_dir,
            exist_ok=True
        )

        checkpoint_path = os.path.join(
            checkpoint_dir,
            checkpoint_name
        )


        for epoch in range(epochs):
            train_loss = 0

            for X,y in train_loader:
                
                X = X.to(model.device)
                y = y.to(model.device)

                optimizer.zero_grad()

                # print("Input Device:", X.device)
                # print("Model Device:", next(model.parameters()).device)

                predictions = model(X)

                loss = criterion(
                    predictions,
                    y
                )

                loss.backward()
                optimizer.step()

                train_loss += loss.item()
            
            train_loss /= len(train_loader)
            model.eval()

            validation_loss = 0

            with torch.no_grad():
                for X, y in validation_loader:
                    X = X.to(model.device)
                    y = y.to(model.device)

                    predictions = model(X)

                    loss = criterion(
                        predictions,
                        y
                    )
                    validation_loss += loss.item()
            validation_loss /= len(validation_loader)
            if validation_loss < best_validation_loss:
                best_validation_loss = validation_loss
                epochs_without_improvement = 0

                torch.save(
                    model.state_dict(),
                    checkpoint_path
                )
                print("✓ Best model saved.")
            else:
                epochs_without_improvement += 1
            model.train()
            
            print(
                f"Epoch {epoch+1}/{epochs}"
                f" | Train : {train_loss:.6f}"
                f" | Validation : {validation_loss:.6f}"
                f" | Best: {best_validation_loss:.6f}"
            )

            if epochs_without_improvement >= patience:

                print("\nEarly stopping triggered.")

                print(
                    f"Best Validation Loss: "
                    f"{best_validation_loss:.6f}"
                )

                break
        return checkpoint_path