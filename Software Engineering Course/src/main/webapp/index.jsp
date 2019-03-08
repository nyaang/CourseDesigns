<%@page contentType="text/html;charset=UTF-8" %>
<%@page import="java.io.*,java.util.*,java.sql.*,task.VisitDB" %>
<%@ page import="com.sun.org.apache.regexp.internal.RE" %>
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>

<body>
<%
    VisitDB db=new VisitDB();
    ResultSet rs=db.executeQuery();
    %>
<a href="history.jsp" style="float: top">已完成任务</a>
<form name="input" action="finish.jsp" method="post">
    工单编号 <input type="text" name="shoporder_no">
    <input type="submit" value="完成该任务">
</form>
<form name="input" action="delete.jsp" method="post">
    <table border="1" style="float:left">
        <tr><th>选中后删除</th><th>工单编号</th> <th>订单数量</th> <th>物料编号</th> <th>工艺路线</th> <th>工单状态</th> <th>订单开始时间</th> <th>订单完成时间</th>  <th>创建时间</th>
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
                <% if (status.equals("1")) { %>
        <tr><th><input type="radio" name="shoporder_no" value=<%=shoporder_no %>></th><th><%=shoporder_no %></th><th><%=shoporder_numbers%></th><th><%=shoporder_item%></th><th><%=process_route%></th>
        <th>未完成
            <%--<% if (status.equals("1")) { %>--%>
                <%--未完成--%>
            <%--<% } else { %>--%>
                <%--已完成--%>
            <%--<% } %>--%>
        </th>
        <th><%=shoporder_start_date%></th><th><%=shoporder_end_date%></th><th><%=create_time%></th></tr>
        <% } %>
    <%
    }
    %>
    </table>
    <input type="submit" value="删除任务">
    </form>
    </form>

    <form style="float:right" action="insert.jsp" method="post">
        工单编号<input type="text" name="shoporder_no"><br>
        订单开始时间<input type="text" name="shoporder_start_date"><br>
        订单完成时间<input type="text" name="shoporder_end_date"><br>
        工艺路线<input type="text" name="process_route"><br>
        物料编号<input type="text" name="shoporder_item"><br>
        订单数量<input type="text" name="shoporder_numbers"><br>
        工单状态<input type="text" name="status"><br>
        创建时间<input type="text" name="create_time"><br>
        <input type="submit" value="增加任务">
    </form>
</body>
</html>
