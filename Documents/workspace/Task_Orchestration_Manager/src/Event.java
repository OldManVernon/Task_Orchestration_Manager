import java.util.GregorianCalendar;

public class Event 
{
private GregorianCalendar date;
private String comments = "";
private String duration = ""; //will figure out how to impliment this later on, is not important functionality yet

	public Event()
	{
		date = new GregorianCalendar();
	}

	public Event(String milestone)
	{
		date = new GregorianCalendar();
		comments = milestone;
	}
	
	public Event(String Date, String milestone)
	{
		TemporalManager temp = new TemporalManager();
		date = temp.StringToDate(Date);
		comments = milestone;
	}
	
	
	public void setDate(GregorianCalendar Date){
		date = Date;
	}
	
	public String toString()
	{
		TemporalManager time = new TemporalManager();
		return time.DateToString(date)+ "-" + comments;
	}
	
	public Event fromString(String event){
		String [] Fields = event.split("-");
		TemporalManager time = new TemporalManager();
		Event temp = new Event(Fields[1]);
		temp.setDate(time.StringToDate(Fields[0]));
		return temp;
	}
}
