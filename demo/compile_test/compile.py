import subprocess
import json

def compile_cpp(file:str):
    filename = file
    outname = filename[:filename.find(".cpp")]
    command = ["g++", "-c", filename, "-o", outname]
    process = subprocess.run(command, capture_output=True)
    if process.returncode == 1:
        return ("Compile error", process.stderr.decode("utf-8"))
    return ("Success", outname)

def compile_java(file:str):
    filename = file
    outname = filename.replace(".java", ".class")
    command = ["javac", filename]
    process = subprocess.run(command, capture_output=True)
    if process.returncode == 1:
        return ("Compile error", process.stderr.decode("utf-8"))
    return ("Success", outname)

def compile_js(file:str):
    filename = file
    command = ["node", filename]
    process = subprocess.run(command, capture_output=True)
    if process.returncode == 1:
        return ("Compile error", process.stderr.decode("utf-8"))
    return ("Success", file)

def compile_python(file:str):
    filename = file
    command = ["python3", "runtime_test/Solution.py"]
    process = subprocess.run(command, capture_output=True)
    if process.returncode == 1:
        return ("Compile error", process.stderr.decode("utf-8"))
    return ("Success", file)

def compile_code(file:str, json_file:str):
    extension = file[file.rfind("."):]
    langDict = {".cpp": compile_cpp,
                ".py": compile_python,
                ".java": compile_java,
                ".js": compile_js
                }
    
    runLangDict = {
        ".cpp": "C++",
        ".py": "python",
        ".java": "Java",
        ".js": "JS"
    }

    res = langDict[extension](str(file))
    json_res = {"Status": res[0], "Message": res[1]} 
    with open(json_file, "w") as file:
        json.dump(json_res, file)
 

    if(res[0] == "Success"):
        if extension == ".cpp":
            subprocess.run(["g++", "/home/sasha/Desktop/demo/runtime_test/chlp.cpp", "-o", "runtime_test/file"], capture_output=True)
        if extension == ".java":
            subprocess.run(["javac", "/home/sasha/Desktop/demo/runtime_test/file.java", "/home/sasha/Desktop/demo/runtime_test/Solution.java"], capture_output=True)
        runtime_res = subprocess.run(["/home/sasha/Desktop/demo/runtime_test/main", runLangDict[extension]], capture_output=True)
        if runtime_res.stderr.decode("utf-8") == "":
            status = "Success"
            if runtime_res.stdout.decode("utf-8") != "true":
                status = "Failed"
            json_res = {"Status": status, "Message": runtime_res.stdout.decode("utf-8")} 
        else:
            json_res = {"Status": "Runtime error", "Message": runtime_res.stderr.decode("utf-8")}

        with open(json_file, "w") as file:
            json.dump(json_res, file)
        return
    with open(json_file, "w") as file:
            json.dump(json_res, file)

