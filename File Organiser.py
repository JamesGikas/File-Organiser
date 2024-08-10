from pathlib import Path

list_files = Path("/Users/jamesgikas/Desktop/To Be Sorted")

for file in list_files.iterdir():
    if file.name != 'DS_Store' and file.is_file():
        old_name = file.stem
        directory = file.parent
        extension = file.suffix

        parts = old_name.split(' - ')
        def checkfolders(new_path):
            if not new_path.exists():
                new_path.mkdir(parents=True, exist_ok=True)
            new_file_path = new_path / file.name
            file.replace(new_file_path)

        if len(parts) == 4:
            name, subject, assignment_type, assignment_name = parts

            if assignment_type == "(S)":
                print(f"{subject}, {assignment_name} - This assignment is a Summative")
            else:
                print(f"{subject}, {assignment_name} - This assignment is a Formative")

            if name == "James Gikas":
                new_path = list_files / "James Gikas" / subject
                checkfolders(new_path)
            else:
                new_path = list_files / name / subject
                checkfolders(new_path)

        else:
            print("This file is a", extension[1:])
            new_path = list_files/extension[1:]
            checkfolders(new_path)











