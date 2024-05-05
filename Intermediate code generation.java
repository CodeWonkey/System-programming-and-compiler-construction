import java.util.*;
public class Main {
public static void main(String[] args) {
String[] a = new String[50];
String[] op = {"+", "-", "*", "/", "%", "^"};
String[] n = {"t0", "t1", "t2", "t3", "t4", "t5"};
String exp;
int count = 0;
Scanner sc = new Scanner(System.in);
System.out.println("Enter the arithmetic Expression \n");
exp = sc.next();
a = exp.split("");
System.out.println("Op\targument1\targument2\tresult obtained\n");
for (int i = 0; i < a.length; i++) {
for (String s : op) {
if (a[i].equals(s)) {
if (count == 0) {
System.out.println(a[i] + "\t" + a[i - 1] + "\t\t" + a[i + 1] + "\t");
} else {
System.out.println(a[i] + "\t" + n[count - 1] + "\t\t" + a[i + 1] + "\t\t" + n[count - 1]);
}
count++;
}
}
}
}
}