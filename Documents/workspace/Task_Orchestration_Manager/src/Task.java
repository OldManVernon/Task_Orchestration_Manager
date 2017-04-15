import java.util.GregorianCalendar;
import java.util.ArrayList;

public class Task 
{
private String name;
private ArrayList<String> Supplies = new ArrayList<String>();
private int Category;
private GregorianCalendar deadline;
private int id;
private int completion;
private ArrayList<Event> history = new ArrayList<Event>();
private ArrayList<GregorianCalendar> Blackout = new ArrayList<GregorianCalendar>();
private int priority;
//private int priority_growth; //impliment adjustment of priority in accordance to duedate proximity
private ArrayList<Task> subtasks = new ArrayList<Task>();
private GregorianCalendar timer;

//constructor for Task, give task a name and an ID
	public Task(String TaskName, int TaskID)
	{
		name = TaskName;
		id = TaskID;
	}
	
//getters for the fields of Task
	public String getName(){ return name;}
	public ArrayList<String> getSupplies() { return Supplies;}
	public int getCategory() { return Category;}
	public GregorianCalendar getDeadline() { return deadline;}
	public int getID() {return id;}
	public int getcompletion() { return completion;}
	public ArrayList<Event> getHistory() { return history;}
	public ArrayList<GregorianCalendar> getBlackouts() { return Blackout; }
	public int getPriority() { return priority;}
	public ArrayList<Task> getSubtasks() { return subtasks;}
	public GregorianCalendar getTimer() { return timer;}

//setters for the fields of Task	
	public ArrayList<String> addSupply(String tool) { 
		Supplies.add(tool);
		return Supplies;}
	public int setCategory(int category_ID) { Category = category_ID; return Category;}
	public GregorianCalendar setDeadline(int year, int month, int dayOfMonth, int hourOfDay, int minute) { 
		deadline = new GregorianCalendar(1900+ year, month, dayOfMonth, hourOfDay, minute);
		return deadline;}
	public int setcompletion(int newCompletion) { completion = newCompletion; return completion;}
	public ArrayList<Event> addHistory(Event Day) { history.add(Day); return history;}
	public ArrayList<GregorianCalendar> setBlackouts(GregorianCalendar Start, GregorianCalendar End) { 
		Blackout.add(Start);
		Blackout.add(End); 
		return Blackout; }
	public int setPriority(int newPriority) {priority = newPriority; return priority;}
	public ArrayList<Task> addSubtasks(Task newSubTask) { subtasks.add(newSubTask); return subtasks;}
	public GregorianCalendar setTimer(GregorianCalendar renew){ timer = renew; return timer;}

//toString method for a Task outputs the details for the Task in a csv format
//nested lists, I.E. Supplies, history, and Blackout times have a ' preceeding each element with a , at the end of the sublist
	public String toString(){
		String temp = "";
/*INDX 1 = NAME*/
		temp = temp + name + ","; 
/*INDX 2 = ID*/		
		temp = temp + id + ",";
/*INDX 3 = SUPPLIES*/
		for (String supply : Supplies)
		{
			temp = temp + "'" + supply;
		}
		temp = temp + ",";
/*INDX 4 = CATEGORY*/
		temp = temp + Category + ",";
		//GregorianCalendar deadline
		//TODO write an interface that converts GregorianCalendar into a Comprehensible String
		//will be useful for the Timer and Blackout fields as well
/*INDX 5 = COMPLETION*/
		temp = temp + completion + ",";
		//private ArrayList<Event> history;
		//TODO Events need their own toString as well
		//private ArrayList<GregorianCalendar> Blackout;
/*INDX 6 = PRIORITY*/
		temp = temp +  priority + ",";
/*INDX 7 = SUBTASKS*/
		for (Task sub : subtasks)
		{
			temp = temp + "'" + sub.getName() + sub.getID();
		}
		//private GregorianCalendar timer;
		
		return temp;
	}
}
