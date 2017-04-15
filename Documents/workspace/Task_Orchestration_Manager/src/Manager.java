import java.util.GregorianCalendar;
import java.util.ArrayList;
import java.util.Date;
import java.io.*;

public class Manager 
{
ArrayList<Task> AllTasks = new ArrayList<Task>();
ArrayList<Task> PossibleTasks = new ArrayList<Task>();
ArrayList<Day> AllHistory = new ArrayList<Day>();
String [] Categories = {"Leisure", "Growth", "Feildmouse", "Antelope"};
	public Manager()
	{
		
	}
	


public static void Main(String [] args)
{
	Manager me = new Manager();
	int trackerID = 0;
	Task temp = new Task("Learn Git", trackerID);
	temp.setPriority(8);
	temp.setCategory(1);
	GregorianCalendar blackstart = new GregorianCalendar(2017, 04, 17, 22, 00); //pretend vacation
	GregorianCalendar blackend = new GregorianCalendar(2017, 04, 19, 22, 00);
	temp.setBlackouts(blackstart, blackend);
	temp.setcompletion(12);//%
	temp.setTimer(new GregorianCalendar(0000, 00, 00, 60, 00));//only need 60 minute sanity breaks between git lessons
	temp.setDeadline(2017, 05, 1, 12, 00);
	me.AllTasks.add(temp);
	
}

}