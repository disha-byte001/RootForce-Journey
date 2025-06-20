# 🐧 Linux Journey - Day 2

## ✅ What I Did Today
- Explored basic terminal navigation commands
- Learned how to move between directories and understand the Linux file system
- Discovered the magic of `cd ..` and how to go back to root

---

## 🔹 Commands Learned

### 1. `pwd` — *Print Working Directory*
Prints the current location you're in within the file system.

$ pwd
/home/user

📌 Congrats! This was my first Linux terminal command ever 😄

2. ls — List
Lists all files and folders in your current directory.

bash
$ ls
Desktop  Documents  Downloads
If you’re in /home/user, you’ll see folders like Documents, Downloads, etc.

3. cd — Change Directory
Used to move between folders.

bash
$ cd Desktop
Now when you run pwd:

bash
$ pwd
/home/user/Desktop

Boom! You’re now inside your Desktop.

4. cd .. — Move Up One Level
Moves you one level back in the directory structure.

🌀 Example Flow:
bash
$ pwd
/home/user/Desktop

$ cd ..
$ pwd
/home/user

$ cd ..
$ pwd
/home

$ cd ..
$ pwd
/


🎉 Boom! You’re in / → the root directory of the entire system.

❓ Quiz: How to go back to /home/user from /
Try using just 2 commands!

✅ Solution:
First, check content of /:

bash
$ ls
bin  boot  dev  etc  home  ...

Move into /home:

bash
$ cd home

#Find your username (e.g., user), then:

bash
$ cd user

#Now check:

bash
$ pwd
/home/user

🥳 That’s it! Clean and simple navigation using just two commands.

