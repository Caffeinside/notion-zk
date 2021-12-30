import os
import webbrowser
from typing import Tuple, List

import inquirer as prompt
from dotenv import load_dotenv
from md2notion.upload import convert, uploadBlock
from notion.client import NotionClient

load_dotenv()

notion_client = NotionClient(token_v2=os.environ.get('NOTION_TOKEN'))
notion_table_id = os.environ.get('NOTION_PAGE')

notion_collection_view = notion_client.get_collection_view(notion_table_id)
notion_collection_view_rows = notion_collection_view.collection.get_rows()


def create() -> None:
    note_content = prompt.editor('Creating your new note')
    new_row = notion_collection_view.collection.add_row()
    rendered_content = convert(note_content)
    new_row.title = _get_first_block_as_title(rendered_content)
    for blockDescriptor in rendered_content:
        uploadBlock(blockDescriptor, new_row, None)


def delete() -> None:
    index, title_to_remove = _select_title()
    if prompt.confirm('Are you sure?'):
        notion_collection_view_rows[index].remove()
        print(f'Removing {title_to_remove}...')


def open() -> None:
    index, title_to_edit = _select_title()
    row = notion_collection_view_rows[index]
    page_url = f'{notion_table_id}&p={row.id.replace("-", "")}'
    webbrowser.open_new_tab(page_url)
    print(f'Opening {title_to_edit}...')


def _select_title() -> Tuple[int, str]:
    titles = [row.title for row in notion_collection_view_rows]
    selected_title = prompt.list_input('Select title', choices=titles)
    index = titles.index(selected_title)
    return index, selected_title


def _get_first_block_as_title(rendered_content: List[dict]):
    return rendered_content[0]['title']
