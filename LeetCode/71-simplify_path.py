"""

https://leetcode.com/problems/simplify-path/

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:
- A single period '.' represents the current directory.
- A double period '..' represents the previous/parent directory.
- Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
- Any sequence of periods that does not match the rules above should be treated as a valid 
  directory or file name. For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:
- The path must start with a single slash '/'.
- Directories within the path must be separated by exactly one slash '/'.
- The path must not end with a slash '/', unless it is the root directory.
- The path must not have any single or double periods ('.' and '..') used to denote current or 
  parent directories.

Return the simplified canonical path.


Example 1:
Input: path = "/home/"
Output: "/home"
Explanation:
The trailing slash should be removed.

Example 2:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation:
Multiple consecutive slashes are replaced by a single one.

Example 3:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:
A double period ".." refers to the directory up a level (the parent directory).

Example 4:
Input: path = "/../"
Output: "/"
Explanation:
Going one level up from the root directory is not possible.

Example 5:
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation:
"..." is a valid name for a directory in this problem.


Constraints:
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'.
- path is a valid absolute Unix path.

--- VARIANT ---

You are provided with an absolute path representing the current working directory cwd in a 
Unix-style file system. Additionally, you are given a relative path, denoted as cd, which instructs
a change to the current working directory. Your tasks to determine and output the simplified 
canonical path that results from applying the relative path, cd, to the Initial cwd.

Return the simplified canonical path.

Example 1:
Input: cwd = "/a/b/c", cd = "/d/./e"
Output: "/d/e"

Example 2:
Input: cwd = "", cd = "/d/./e"
Output: "/d/e"

Example 3:
Input: cwd = "/a/b/c", cd = ""
Output: "/a/b/c"

Example 4:
Input: cwd = "/a/b", cd = ".//c/../../d/f"
Output: "/a/d/f"

"""

def simplifyPath(path: str) -> str:
    path_list = path.split('/')
    stack = []

    for name in path_list:
        if name == "..":
            if stack:
                stack.pop()
            else:
                continue
        elif name == "" or name == ".":
            continue
        else:
            stack.append(name)
    
    if stack:
        return "/" + "/".join(stack)
    else:
        return "/"
    
def simplifyPathVariant(cwd: str, cd: str) -> str:
    if cd == "" or cd == ".":
        return cwd

    if cd.startswith('/'):
        cwd = ""
    
    path_list = cwd.split('/') + cd.split('/')
    stack = []

    for name in path_list:
        if name == "..":
            if stack:
                stack.pop()
            else:
                continue
        elif name == "" or name == ".":
            continue
        else:
            stack.append(name)
    
    if stack:
        return "/" + "/".join(stack)
    else:
        return "/"

if __name__ == "__main__":
    # Test Case 1
    path = "/home/"
    print(simplifyPath(path))

    # Test Case 2
    path = "/home//foo/"
    print(simplifyPath(path))

    # Test Case 3
    path = "/home/user/Documents/../Pictures"
    print(simplifyPath(path))

    # Test Case 4
    path = "/../"
    print(simplifyPath(path))

    # Test Case 5
    path = "/.../a/../b/c/../d/./"
    print(simplifyPath(path))

    # --- Testing Variant ---
    # Test Case 1
    cwd = "/a/b/c"
    cd = "/d/./e"
    print(simplifyPathVariant(cwd, cd))

    # Test Case 2
    cwd = ""
    cd = "/d/./e"
    print(simplifyPathVariant(cwd, cd))

    # Test Case 3
    cwd = "/a/b/c"
    cd = ""
    print(simplifyPathVariant(cwd, cd))

    # Test Case 4
    cwd = "/a/b"
    cd = ".//c/../../d/f"
    print(simplifyPathVariant(cwd, cd))