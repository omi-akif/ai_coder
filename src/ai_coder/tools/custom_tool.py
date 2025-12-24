from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os

class FileWriterInput(BaseModel):
    """Input schema for FileWriterTool."""
    filename: str = Field(..., description="The name of the file to write to (e.g., 'hello.py').")
    content: str = Field(..., description="The content to write into the file.")

class FileWriterTool(BaseTool):
    name: str = "File Writer"
    args_schema: Type[BaseModel] = FileWriterInput
    description: str = (
        "Useful for writing code, configuration, or text to a file. "
        "It takes a filename and content as input and saves the file to the current directory."
    )

    def _run(self, filename: str, content: str) -> str:
        try:
            with open(filename, 'w') as f:
                f.write(content)
            return f"Successfully wrote to file: {filename}"
        except Exception as e:
            return f"Error writing to file {filename}: {str(e)}"


class FileReadInput(BaseModel):
    """Input schema for FileReadTool."""
    filename: str = Field(..., description="The name of the file to read.")

class FileReadTool(BaseTool):
    name: str = "File Reader"
    args_schema: Type[BaseModel] = FileReadInput
    description: str = "Useful for reading the contents of a file. It takes a filename as input."

    def _run(self, filename: str) -> str:
        try:
            if not os.path.exists(filename):
                return f"Error : {filename} does not exist."
            with open(filename, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file {filename}: {str(e)}"


class ListDirectoryInput(BaseModel):
    """Input schema for ListDirectoryTool."""
    directory: str = Field(default=".", description="The directory to list files from. Defaults to current directory.")

class ListDirectoryTool(BaseTool):
    name: str = "List Directory"
    description: str = "Useful for seeing what files are in a directory."
    args_schema: Type[BaseModel] = ListDirectoryInput

    def _run(self, directory: str = ".") -> str:
        try:
            files = os.listdir(directory)
            return "\\n".join(files)
        except Exception as e:
            return f"Error listing directory {directory}: {str(e)}"
    