# git 入门操作

## 本地操作

### 设置签名

git config 

![image-20220227195133624](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220227195133624.png)

![image-20220227195344265](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220227195344265.png)

.git里的东西不能乱动

### 添加文件：

git add 

添加文件:先创建文件，提交到暂存区，用来跟踪仓库的文件。不放在本地库的文件git是不管理的

### 提交文件

git commit

🔸注意：引号一定要带，不然会进入一个奇奇怪怪的地方，然后加上”就ok了

#### 参数 -m

1. 这个参数是commit必须要带的，不带就会直接进入默认编辑器
2. 进入默认编辑器使用  :q！退出

#### 参数- a（放在-m的后面）

 将会提交暂存区的所有文件（已跟踪的文件）

#### 参数 --amend

撤销操作，相当于将历史版本给删除 然后再一次提交新的文件

![image-20220301092105450](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220301092105450.png)

### 查看仓库状态

git status

![image-20220227202101784](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220227202101784.png)

🔸注意：添加文件要及时提交add重新添加以及commit

### 查看日志

git log

#### 相关操作

1. ：向后走
2. b上一页
3. q退出

#### 参数--oneline

git log --oneline

![image-20220227205003918](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220227205003918.png)

#### 参数--pretty

将历史日志用一行输出

![image-20220227204937404](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220227204937404.png)

git log --pretty=format  .....

![image-20220301091656995](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220301091656995.png)

#### 参数--stat

项在每次提交的下面列出所有被修改过的文件、有多少文件被修改了以及被修改过 的文件的哪些行被移除或是添加了。 在每次提交的最后还有一个总结。

#### 样式reflog

![image-20220227205103232](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220227205103232.png)



### 回退历史版本

git reset

还可以通过reset HEAD 回退到当前指针指向的索引

![image-20220228221632886](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220228221632886.png)

#### 参数 --hard [索引]

可以往前和往后，hard使本地库和暂存区和工作区都进行了回退

#### 参数--mixed [索引]

后两个动，工作区的不动

#### 参数--soft [索引]

就第三个移动，但是暂存区和工作区都不动

但是一般都是利用hard参数

### 文件的移动(改名)

git mv file_from filr_to

一般用来改名

### 文件的删除

rm 文件名(只在工作区删除了)

后面还要同步暂存区和本地库

![image-20220301190757033](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220301190757033.png)

只是动了一个指针，并不是真正的删除，所以还是可以重新弄到工作区

### 信息差异比对

说明：本身只显示尚未暂存的改动，而不是自上次提交以来所做的所有改动。

#### git diff [filename]

工作区和暂存区比较，还可以和索引加文件名，HEAD

#### git diff  

工作区里的所有不同

#### git diff --staged

 这条命令将比对已暂存 文件与最后一次提交的文件差异

#### git diff --cached

 查看已经暂存起来的变化

### 分支操作

#### git branch [branchname]

开辟分支，会复制主干上的最新版本来独立开发，并行开发

![image-20220301092956855](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220301092956855.png)

#### git branch -v

显示分支： 显示所有的主干及分支

![image-20220301093113871](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220301093113871.png)

🔸这里显示的是两者的版本一样

#### git checkout [branchname]

切换分支，可以在主干上和其他分支上来回切换

#### cat [文件名]

查看分支里的文件信息

#### git merge [branchname]

1. 分支的合并，在其中一个分支上然后来融合其他的分支

![image-20220301182908577](C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220301182908577.png)

 	2. 处理冲突：显示处于合并状态中出现冲突,在同一个文件中修改，会出现冲突，自行修改，然后确定留下哪个，删除不需要的东西，		然后再提交（不带文件名）然后就会取消合并状态。

## 远端操作

以github为例

### 本地仓库的初始化

#### mkdir [respname]

创建本地仓库

#### git init

本地库初始化

远程库的创建

### 创建远端库的地址的别名

- 可在git本地进行别名

#### git remote -v

查看别名

#### git remote add [remoteRespName] [address]

创建别名

### 切换到远程库的不同分支

git checkout [网站别名] / [branchname]

### 推送数据

git push [别名] [branchname]

推送branch中的数据到远程库的分支（如果一开始没有就回创建新的分支，默认第一个为master）

### 克隆操作

将远程库的东西拉取到本地库

git clone [address]

克隆的命令的作用

1. 初始化本地库
2. 将远程库的内容完整的复制下来
3. 替我们创建别名

### 邀请加入团队

1. 登陆管理员的账号

2. 邀请其他成员

   <img src="C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20220301200525259.png" alt="image-20220301200525259" style="zoom:67%;" />

### 远程操作 pull操作

相当于fetch & merge 操作

一般代码简单就可以直接pull [远程库别名]  [branchname]

### 解决协同开发的冲突

当两个人同时修改了同一个文件时，第二个修改者的推送将会失败

1. 先应该拉取下来
2. 要查看冲突，然后就人为解决
3. 然后修改冲突，在推送到远程服务器
