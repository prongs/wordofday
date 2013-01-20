
import javax.swing.JEditorPane;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import java.io.*;

public class Main {
  public static void main(String[] args) throws Exception {
    JEditorPane editor = new JEditorPane("text/html",
        "<H1>A!</H1><P><FONT COLOR=blue>blue</FONT></P>");
    editor.setEditable(false);
    JScrollPane pane = new JScrollPane(editor);
	BufferedReader br= new BufferedReader(new FileReader(args[0]));
	String buf, line;
	buf="";
	while((line=br.readLine())!=null)
	{
		buf+=line;
		buf+="\n";
	}
    JFrame f = new JFrame("Hey");
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.getContentPane().add(pane);
    f.setSize(800, 600);
	editor.setText(buf);
    f.setVisible(true);
  }
}
