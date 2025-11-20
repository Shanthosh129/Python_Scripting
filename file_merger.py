import os

input_folder = "inputfolder"
output_file = "merged_output.txt"

with open(output_file ,"w") as out_file:
    print(f"Starting merge operation. Reading from'{input_folder}'")

    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' not found. Please create it and place your text files inside.")
        exit()

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder,filename)
            print(f"  -> Merging: {filename}")
            try:
                with open(file_path,"r") as infile:
                    out_file.write(infile.read() +"\n")
            except Exception as e:
                print(f"Couldn't read file {filename}, error: {e}")
print(f"Merging complete! Output saved to '{output_file}'")