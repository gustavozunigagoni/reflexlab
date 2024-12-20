import reflex as rx
from typing import List, Any
class State(rx.State):
    clicked_data: str = "Cell clicked: "

    cols: list[Any] = [
        {"title": "Title", "type": "str"},
        {
            "title": "Name",
            "type": "str",
            "group": "Data",
            "width": 300,
        },
        {
            "title": "Birth",
            "type": "str",
            "group": "Data",
            "width": 150,
        },
        {
            "title": "Human",
            "type": "bool",
            "group": "Data", 
            "width": 80,
        },
        {
            "title": "House",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Wand",
            "type": "str",
            "group": "Data",
            "width": 250,
        },
        {
            "title": "Patronus",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Blood status",
            "type": "str",
            "group": "Data",
            "width": 200,
        },
    ]

    data = [
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
[
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11' Holly phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3", 
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "103⁄4' vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],        
    ]

    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)

    def get_clicked_data(self, pos) -> str:
        self.clicked_data = f"Cell clicked: {pos}"



@rx.page(route="/page13", title="page13")
def page13():
    return rx.data_editor(
        columns=State.cols,
        header_height=60,
        group_header_height=50,
        data=State.data,
        on_cell_clicked=State.click_cell,
        smooth_scroll_x=True,
        smooth_scroll_y=True,
        row_height=25,
        freeze_columns=1,
        column_select="multi",
        overscroll_x=10,
    )
