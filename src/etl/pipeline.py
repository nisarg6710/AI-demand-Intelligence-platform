from src.etl.validate import DataValidator
from src.observability.metrics import ETLMetrics


class ETLPipeline:

    @staticmethod
    def run(config, loader):
        metrics = ETLMetrics()

        metrics.start()

        data = config.extractor(
            config.source_path,
            chunksize=config.chunksize
        )

        if config.chunksize is None:

            ETLPipeline._process_dataframe(
                data,
                config,
                loader
            )

            metrics.add_rows(len(data))
            metrics.add_chunk()

        else:

            chunk_number = 1

            for chunk in data:

                print(
                    f"Processing chunk {chunk_number}..."
                )

                ETLPipeline._process_dataframe(
                    chunk,
                    config,
                    loader
                )
                metrics.add_rows(len(chunk))

                metrics.add_chunk()

                print(f"Chunk {chunk_number} completed.")

                chunk_number += 1


        metrics.stop()
        metrics.summary()

        print(
            f"{config.target_table} loaded successfully."
        )
    
    

    @staticmethod
    def _process_dataframe(df, config, loader):

        DataValidator.validate_not_empty(df)

        ## Validate before transformation
        if config.input_required_columns:
            DataValidator.validate_columns(
                df,
                config.input_required_columns
            )

        ## Transform
        df = config.transformer(df)

        ## Validate after transformation
        if config.output_required_columns:
            DataValidator.validate_columns(
                df,
                config.output_required_columns
            )

        ## Check for null values aftertransformation
        if config.output_null_check_columns:
            DataValidator.validate_nulls(
                df,
                config.output_null_check_columns
            )

        loader.load_dataframe(
            df,
            config.target_table
        )