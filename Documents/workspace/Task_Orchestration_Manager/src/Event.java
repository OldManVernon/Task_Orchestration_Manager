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
	
	public String toString()
	{
		TemporalManager time = new TemporalManager();
		return time.DateToString(date)+ "-" + comments;
	}
}
