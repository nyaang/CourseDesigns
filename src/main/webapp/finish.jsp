<%--
  Created by IntelliJ IDEA.
  User: Aotome
  Date: 2018/7/7
  Time: 15:13
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@page import="java.io.*,java.util.*,java.sql.*,task.VisitDB" %>
<%@ page import="com.sun.org.apache.regexp.internal.RE" %>
<html>
<head>
    <title>Success</title>
</head>
<body>
任务完成
<%
    String shoporder_no=request.getParameter("shoporder_no");
    VisitDB db=new VisitDB();
    db.update(shoporder_no);
%>

</body>
</html>
