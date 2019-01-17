# Utils
找回被stash drop掉的记录
git fsck --lost-found
将命令行输出全部拷贝放进file.txt 
命令行执行脚本即可 可以通过代码关键字找到改动代码，然后下面有git show XXXXX 说明，XXXXX就是丢失的commit
之后git merge XXXXX即可
