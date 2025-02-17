import argilla as rg
import os

# settings=rg.Settings(
#     fields=[
#         rg.TextField(name="system_prompt"),
#         rg.TextField(name="prompt"),
#         rg.TextField(name="completion"),
#     ],
#     questions=[
#         rg.RatingQuestion(
#             name="rating",
#             values=[1, 2, 3, 4, 5],
#             title="Does this training sample make sense?",
#             description="1 = Makes no sense - 5 = Makes a lot of sense",
#             required=True,
#         )
#     ],
# ),

def create_dataset(
    name: str,
    workspace: str,
    settings: rg.Settings
):
    dataset = rg.Dataset(
        name=name,
        workspace=workspace,
        settings=settings
    )

    # Might error if dataset already exists
    try:
        dataset.create()
    except:
        pass

class SimpleArgillaDatasetClient:
    def __init__(
        self,
        name: str,
        workspace: str
    ):
        self._client = rg.Argilla(
            api_url=os.getenv("ARGILLA_API_URL"),
            api_key=os.getenv("ARGILLA_API_KEY"),

        )

        self.dataset = self._client.datasets(
            name=name,
            workspace=workspace
        )
    
    def delete_records(self, records_to_delete: list[rg.Record]):
        self.dataset.records.delete(
            records=records_to_delete
        )
    
    def upsert_records(self, records_to_upsert: list[rg.Record]):
        self.dataset.records.log(
            records=records_to_upsert
        )
    
    def clear_dataset(self):
        self.delete_records(list(self.dataset.records))
