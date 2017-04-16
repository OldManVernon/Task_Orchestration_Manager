import java.util.GregorianCalendar;
import java.util.ArrayList;
import java.util.Date;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class Manager 
{
ArrayList<Task> AllTasks = new ArrayList<Task>();
ArrayList<Task> PossibleTasks = new ArrayList<Task>();
ArrayList<Day> AllHistory = new ArrayList<Day>();
String [] Categories = {"Leisure", "Growth", "Feildmouse", "Antelope"};
private final int NAME = 0;
private final int ID = 1;
private final int SUPPLIES = 2;
private final int CATEGORY = 3;
private final int COMPLETION = 4;
private final int PRIORITY = 5;
private final int SUBTASKS = 6;
private final int DEADLINE = 7;
private final int TIMER = 8;
private final int BLACKOUT = 9;
private final int EVENTS = 10;
private final int YEAR = 0;
private final int MONTH = 1;
private final int DAY = 2;
private final int HOUR = 3;
private final int MINUTE = 4;

	public Manager()
	{

	}

	public ArrayList<Task> ReadData(String Filelocation)
	{   //example filepath
		//File fileloc = new File("/Users/mortum987789/Desktop//HourlyDemands_2002-2014.csv");
		BufferedReader br = null;
		File fileloc = new File(Filelocation);
		
		//attempt to open the file
		try {
			br = new BufferedReader(new FileReader(fileloc));} 
		
		catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();}
		
		//Here is where our process really begins
	    try {
	        StringBuilder sb = new StringBuilder();
	        String line = br.readLine();    
	    	while (line != null)
	    	{
	    		String [] temp = line.split(",");
	    		//for(String indx : temp)
	    		//	System.out.println(indx);
	    		Task tempTask = new Task(temp[NAME], Integer.parseInt(temp[ID]));
	    		String [] temporaryer = temp[SUPPLIES].split("'");
	    		for (String supply : temporaryer)
	    			tempTask.addSupply(supply);
	    		tempTask.setCategory(Integer.parseInt(temp[CATEGORY]));
	    		tempTask.setcompletion(Integer.parseInt(temp[COMPLETION]));
	    		tempTask.setPriority(Integer.parseInt(temp[PRIORITY]));
	    		temporaryer = temp[SUBTASKS].split("'");
	    		for (String sub : temporaryer){
	    			String [] subTask = sub.split(":");
	    			tempTask.addSubtasks(new Task(subTask[NAME], Integer.parseInt(subTask[ID])));
	    		}
	    		
	    		line = br.readLine();  
	    	}
	    }
	    catch (IOException e) 
	    {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
	    
	    finally 
		{
	    	try 
	    	{
			br.close();
	    	}
	    	catch (IOException e) 
	    	{
			// TODO Auto-generated catch block
			e.printStackTrace();
	    	}
	    }
		ArrayList<Task> readTasks = new ArrayList<Task>();
		return readTasks;
	}
}