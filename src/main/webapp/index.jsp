<%@page contentType="text/html;charset=UTF-8" %>
<%@page import="java.io.*,java.util.*,java.sql.*,task.VisitDB" %>
<%@ page import="com.sun.org.apache.regexp.internal.RE" %>
<html>
<body>
<%
    VisitDB db=new VisitDB();
    ResultSet rs=db.executeQuery();
    %>
    <table border="1">
        <tr><th>工单编号</th> <th>订单数量</th> <th>物料编号</th> <th>工艺路线</th> <th>工单状态</th> <th>订单开始时间</th> <th>订单完成时间</th>  <th>创建时间</th>
        <%
    while (rs.next()) { //遍历数据库查询的返回对象

        String shoporder_no = rs.getString("shoporder_no");
        String shoporder_numbers = rs.getString("shoporder_numbers");
        String shoporder_item = rs.getString("shoporder_item");
        String process_route = rs.getString("process_route");
        String status = rs.getString("status");
        String shoporder_start_date = rs.getString("shoporder_start_date");
        String shoporder_end_date = rs.getString("shoporder_end_date");
        String create_time = rs.getString("create_time");
%>

        <tr><th><%=shoporder_no %></th><th><%=shoporder_numbers%></th><th><%=shoporder_item%></th><th><%=process_route%></th><th><%=status%></th><th><%=shoporder_start_date%></th><th><%=shoporder_end_date%></th><th><%=create_time%></th></tr>
    <%
    }
    %></table>
</body>
</html>
