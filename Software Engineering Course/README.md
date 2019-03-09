# 软件工程课程设计

​	采用MVC设计模式。使用 Maven 构建依赖库。项目的目录结构如下：

shengchanbudemo——根目录

​	src——src 目录

​		main——main 目录

​			java——java 目录，用于存放.java 文件。

​				task——task 子目录。

​					VisitDB.java——所有对数据库增删改查的操作都在 VisitDB.java。

​			resources——resources 目录。用于存放一些外部依赖。暂未用到。

​			webapp——网站根目录

​				WEB-INF——WEB-INF 目录下存放有 web.xml。

​					web.xml

​				delete.jsp——用于删除一个任务工单。

​				finish.jsp——用于把未完成的任务工单转为已完成的任务工单。

​				history.jsp——用于查看已经完成的历史任务工单。

​				index.jsp——网站主页。

​				insert.jsp——用于新增一个任务工单。

target——编译输出的 target 目录。该目录下的文件都是输出缓存文件。

pom.xml——Maven 的配置文档。

shengchanbudemo.iml