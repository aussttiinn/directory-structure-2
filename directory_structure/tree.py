import pathlib
import emoji

EMOJI_BASE = emoji.emojize(':open_file_folder:')
EMOJI_FOLDER = emoji.emojize(':file_folder:')
EMOJI_FILE = emoji.emojize(':page_facing_up:')

class Tree:
    """
    A class to generate directory tree structures recursively.
    
    Parameters
    ----------
    path : str
        The directory path, it can be in any valid format.
    absolute : bool, default False
        Set it to True if you want to use the absolute path.
    max_depth : int, default None
        Maximum depth for recursive traversal. None means no limit.
    """
    def __init__(self, path: str, absolute: bool = False, max_depth: int = None) -> None:
        self.path = pathlib.Path(path)
        self.absolute = absolute
        self.max_depth = max_depth
        self._lines = 0
        self._base = []
        self._content = []
        self._tree = self._make_tree()

    def _space(self, extra_depth: int = 0) -> str:
        """
        Return a string containing spaces according to the folder or file location.
        
        Parameters:
        -----------
        extra_depth : int
            Additional depth for recursive content
            
        Returns:
        --------
        spaces : str
            String containing spaces.
        """
        return f'\n{"  " * (self._lines + extra_depth)}'

    def _get_base(self) -> None:
        """
        Depending on the absolute attribute, get all or only the last folder
        of the path.
        """
        self.path = self.path.resolve()
        if self.absolute:
            if isinstance(self.path, pathlib.WindowsPath):
                self._base.append(f'{EMOJI_BASE} {self.path.drive}')
            elif isinstance(self.path, pathlib.PosixPath):
                self._base.append(f'{EMOJI_BASE} {self.path.root}')
            directories = self.path.parts[1:]
            for directory in directories:
                self._base.append(f'{self._space()}|_{EMOJI_BASE} {directory}')
                self._lines = len(self._base) - 1
        else:
            directory = self.path.name
            self._base.append(f'{EMOJI_BASE} {directory}')

    def _get_content(self, current_path: pathlib.Path, depth: int = 0) -> None:
        """
        Recursively get all folders and files from the directory content.
        
        Parameters:
        -----------
        current_path : pathlib.Path
            The current directory path being processed
        depth : int
            Current depth in the recursive tree
        """
        if self.max_depth is not None and depth >= self.max_depth:
            return

        # Sort items to ensure consistent ordering
        items = sorted(current_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        
        for item in items:
            if item.is_dir():
                self._content.append(
                    f'{self._space(depth)}|_{EMOJI_FOLDER} {item.name}'
                )
                # Recurse into the subdirectory
                self._get_content(item, depth + 1)
            else:
                self._content.append(
                    f'{self._space(depth)}|_{EMOJI_FILE} {item.name}'
                )

    def _make_tree(self) -> str:
        """
        Call other private methods and then sum its joined results to make the
        directory tree structure.
        
        Returns:
        --------
        tree : str
            Complete directory tree structure.
        """
        # Handle the path traversal exactly as before
        self._get_base()
        self._base = ''.join(self._base)
        
        # Start recursive traversal only at the final directory
        self._get_content(self.path)
        self._content = ''.join(self._content)
        
        tree = self._base + self._content
        return tree

    def __str__(self) -> str:
        return self._tree