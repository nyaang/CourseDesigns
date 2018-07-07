<%--
  Created by IntelliJ IDEA.
  User: Aotome
  Date: 2018/7/7
  Time: 12:02
  To change this template use File | Settings | File Templates.
--%>
<%@page contentType="text/html;charset=UTF-8" %>
<%@page import="java.io.*,java.util.*,java.sql.*,task.VisitDB" %>
<%@ page import="com.sun.org.apache.regexp.internal.RE" %>
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Success</title>
</head>
<body>
下达任务成功

<%
    String shoporder_no=request.getParameter("shoporder_no"); //从表单获得
    String shoporder_start_date=request.getParameter("shoporder_start_date"); //从表单获得
    String shoporder_end_date=request.getParameter("shoporder_end_date"); //从表单获得
    String process_route=request.getParameter("process_route"); //从表单获得
    String shoporder_item=request.getParameter("shoporder_item"); //从表单获得
    String status=request.getParameter("status"); //从表单获得
    String shoporder_numbers=request.getParameter("shoporder_numbers"); //从表单获得
    String create_time=request.getParameter("create_time"); //从表单获得
    VisitDB db=new VisitDB();
//    db.insert("123","2017-08-26","2017-08-26","213","ddd","1","1","2017-08-26");
    db.insert(shoporder_no,shoporder_start_date,shoporder_end_date,process_route,shoporder_item,status,shoporder_numbers,create_time);
%>
</body>
</html>
