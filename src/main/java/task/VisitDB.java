package task;

import java.sql.*;

public class VisitDB {
    private Connection conn = null;
    private PreparedStatement stmt = null;
    ResultSet rs = null;
    public static final String driverName = "com.mysql.jdbc.Driver";
    public static final String urls = "jdbc:mysql://10.2.213.98/jsp2018?user=jsp&password=jsp"+ "&useUnicode=true&characterEncoding=utf-8";
    public VisitDB(){}

    public ResultSet executeQuery() throws Exception {
        rs = null;
        try {
            Class.forName(driverName);
            conn = DriverManager.getConnection(urls);
            stmt = conn.prepareStatement("select * from ly_shoporder"); //此处设置表名
            rs = stmt.executeQuery();
        } catch (SQLException e) {
            throw e;
        } catch (Exception e) {
            throw e;
        }
        return rs;
    }
}
