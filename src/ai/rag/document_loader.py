from pathlib import Path

class DocumentLoader:

    def __init__(
            self,
            knowledge_base='data/knowledge_base'
    ):
        
        self.knowledge_base = Path(
            knowledge_base
        )
    
    def load_documents(self):

        documents = []

        for file in self.knowledge_base.rglob('*.md'):

            with open(
                file,
                'r',
                encoding='utf-8'
            ) as f:
                
                documents.append(

                    {
                        'path': str(file),

                        'name': file.name,

                        'category': file.parent.name,

                        'content': f.read()
                    }
                )
        
        return documents