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
		ArrayList<Task> readTasks = new ArrayList<Task>();
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
	        TemporalManager thyme = new TemporalManager();
	    	while (line != null)
	    	{
	    		String [] temp = line.split(",");
	    		System.out.println("Below is what the line was read in as and split into on the \",\"");
	    		for(String indx : temp)
	    			System.out.println(indx);
	    		Task tempTask = new Task(temp[NAME], Integer.parseInt(temp[ID]));
	    		String [] temporaryer = temp[SUPPLIES].split("'");
	    		for (int indx = 1; indx < temporaryer.length; indx ++)
	    			tempTask.addSupply(temporaryer[indx]);
	    		tempTask.setCategory(Integer.parseInt(temp[CATEGORY]));
	    		tempTask.setcompletion(Integer.parseInt(temp[COMPLETION]));
	    		tempTask.setPriority(Integer.parseInt(temp[PRIORITY]));
	    		temporaryer = temp[SUBTASKS].split("'");
	    		System.out.println("Below is what the subtasks was read in as and split into on the \'");
	    		for(String indx : temporaryer)
	    			System.out.println(indx);
	    		for (int indx = 1; indx < temporaryer.length; indx ++){
	    			String [] subTask = temporaryer[indx].split(":");
	    			tempTask.addSubtasks(new Task(subTask[NAME], Integer.parseInt(subTask[ID])));
	    		}
	    		temporaryer = temp[DEADLINE].split(":");
	    		tempTask.setDeadline(Integer.parseInt(temporaryer[YEAR]), Integer.parseInt(temporaryer[MONTH]), 
	    				Integer.parseInt(temporaryer[DAY]), Integer.parseInt(temporaryer[HOUR]), Integer.parseInt(temporaryer[MINUTE]));
	    		temporaryer = temp[TIMER].split(":");
	    		GregorianCalendar renew = new GregorianCalendar(Integer.parseInt(temporaryer[YEAR]), Integer.parseInt(temporaryer[MONTH]), 
	    				Integer.parseInt(temporaryer[DAY]), Integer.parseInt(temporaryer[HOUR]), Integer.parseInt(temporaryer[MINUTE]));
	    		tempTask.setTimer(renew);
	    		temporaryer = temp[BLACKOUT].split("'");
	    		String [] blackoutHelper = {""};
	    		String [] dateSplitter = {""};
	    		for (int indx = 1; indx < temporaryer.length; indx++)
	    		{
	    			blackoutHelper = temporaryer[indx].split("-");
	    			dateSplitter = blackoutHelper[0].split(":");
	    			GregorianCalendar start = new GregorianCalendar(Integer.parseInt(dateSplitter[YEAR]), Integer.parseInt(dateSplitter[MONTH]), 
		    				Integer.parseInt(dateSplitter[DAY]), Integer.parseInt(dateSplitter[HOUR]), Integer.parseInt(dateSplitter[MINUTE]));
	    			dateSplitter = blackoutHelper[1].split(":");
	    			GregorianCalendar end = new GregorianCalendar(Integer.parseInt(dateSplitter[YEAR]), Integer.parseInt(dateSplitter[MONTH]), 
		    				Integer.parseInt(dateSplitter[DAY]), Integer.parseInt(dateSplitter[HOUR]), Integer.parseInt(dateSplitter[MINUTE]));
	    			tempTask.addBlackouts(start, end);
	    		}
	    		temporaryer = temp[EVENTS].split("'");
	    		String [] eventSplitter = {""};
	    		for (int indx = 1; indx < temporaryer.length; indx++)
	    		{
	    			eventSplitter = temporaryer[indx].split("-");
	    			Event tempEv = new Event(eventSplitter[0], eventSplitter[1]);
	    			tempTask.addHistory(tempEv);
	    		}
	    		readTasks.add(tempTask);
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
		return readTasks;
	}
}