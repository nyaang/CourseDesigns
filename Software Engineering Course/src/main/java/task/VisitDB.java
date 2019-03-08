package task;

import java.sql.*;

public class VisitDB {
    private Connection conn = null;
    private PreparedStatement stmt = null;
    ResultSet rs = null;
    public static final String driverName = "com.mysql.jdbc.Driver";
//    public static final String urls = "jdbc:mysql://10.2.213.98:3306/jsp2018?user=jsp&password=jsp"+ "&useUnicode=true&characterEncoding=utf-8";
    public static final String urls = "jdbc:mysql://localhost/jsp2018?user=root&password=root"+ "&useUnicode=true&characterEncoding=utf-8";
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
    public void insert(String shoporder_no,String shoporder_start_date,String shoporder_end_date,String process_route,String shoporder_item,String status,String shoporder_numbers,String create_time) throws Exception{
        try {
            Class.forName(driverName);
            conn = DriverManager.getConnection(urls);
            stmt = conn.prepareStatement("INSERT INTO ly_shoporder(`shoporder_no`, `shoporder_start_date`, `shoporder_end_date`, `process_route`, `create_time`, `shoporder_item`, `shoporder_numbers`, `status`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"); //此处设置表名
            stmt.setString(1,shoporder_no);
            stmt.setString(2,shoporder_start_date);
            stmt.setString(3,shoporder_end_date);
            stmt.setString(4,process_route);
            stmt.setString(5,create_time);
            stmt.setString(6,shoporder_item);
            stmt.setString(7,shoporder_numbers);
            stmt.setString(8,status);
            stmt.executeUpdate();
        } catch (SQLException e) {
            throw e;
        } catch (Exception e) {
            throw e;
        }
    }
    public void delete(String shoporder_no)throws Exception{
        try {
            Class.forName(driverName);
            conn = DriverManager.getConnection(urls);
            stmt = conn.prepareStatement("delete from ly_shoporder where shoporder_no=?"); //此处设置表名
            stmt.setString(1,shoporder_no);
            stmt.executeUpdate();
        } catch (SQLException e) {
            throw e;
        } catch (Exception e) {
            throw e;
        }
    }
    public void update(String shoporder_no)throws Exception{
        try {
            Class.forName(driverName);
            conn = DriverManager.getConnection(urls);
            stmt = conn.prepareStatement("update ly_shoporder set status=2 where shoporder_no=?"); //此处设置表名
            stmt.setString(1,shoporder_no);
            stmt.executeUpdate();
        } catch (SQLException e) {
            throw e;
        } catch (Exception e) {
            throw e;
        }
    }
}
