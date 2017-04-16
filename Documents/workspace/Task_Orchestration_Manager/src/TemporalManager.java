import java.util.GregorianCalendar;

public class TemporalManager 
{
	public TemporalManager()
	{
		
	}
	
//returns the number of days between end and start dates
	public int Daysdifference(GregorianCalendar start, GregorianCalendar end)
	{
	int day = end.get(GregorianCalendar.DAY_OF_MONTH) - start.get(GregorianCalendar.DAY_OF_MONTH);
	//the difference in day of the month can easily be negative, iff the start and end are in different months or years
		
	if (end.get(GregorianCalendar.YEAR) != start.get(GregorianCalendar.YEAR) || end.get(GregorianCalendar.MONTH) != start.get(GregorianCalendar.MONTH)){
		int accumulator = 0; //keeps track of the number of days between start and finish
		
		GregorianCalendar stepper = new GregorianCalendar(start.get(GregorianCalendar.YEAR), start.get(GregorianCalendar.MONTH), start.get(GregorianCalendar.DAY_OF_MONTH), start.get(GregorianCalendar.HOUR_OF_DAY), start.get(GregorianCalendar.MINUTE));
		accumulator += stepper.getActualMaximum(GregorianCalendar.DAY_OF_MONTH) - stepper.get(GregorianCalendar.DAY_OF_MONTH); //number of days remaining in that month
		//finish up the month that the start date is in the middle of, the fact that dates index @ 0 means the difference is already accurate
		
		//step forward one month, which sometimes means January of the next year
		if (stepper.get(GregorianCalendar.MONTH) == 11){
			stepper = new GregorianCalendar(start.get(GregorianCalendar.YEAR)+1, start.get(GregorianCalendar.MONTH), start.get(GregorianCalendar.DAY_OF_MONTH), start.get(GregorianCalendar.HOUR_OF_DAY), start.get(GregorianCalendar.MINUTE));}
		else{
			stepper = new GregorianCalendar(start.get(GregorianCalendar.YEAR), start.get(GregorianCalendar.MONTH)+1, start.get(GregorianCalendar.DAY_OF_MONTH), start.get(GregorianCalendar.HOUR_OF_DAY), start.get(GregorianCalendar.MINUTE));}
		
		//while we haven't reached the end month
			while ( stepper.get(GregorianCalendar.YEAR) < end.get(GregorianCalendar.YEAR) || (stepper.get(GregorianCalendar.MONTH) < end.get(GregorianCalendar.MONTH))){
				//System.out.println(stepper.get(GregorianCalendar.MONTH));
				accumulator += stepper.getActualMaximum(GregorianCalendar.DAY_OF_MONTH); //every day that occured in the month gets added. GregorianCalendar accounts for leap years and w/e
				//step forward one month, which sometimes means January of the next year
				if (stepper.get(GregorianCalendar.MONTH) == 11)
					stepper = new GregorianCalendar(stepper.get(GregorianCalendar.YEAR)+1, 0, stepper.get(GregorianCalendar.DAY_OF_MONTH), start.get(GregorianCalendar.HOUR_OF_DAY), start.get(GregorianCalendar.MINUTE));
				else 
					stepper = new GregorianCalendar(stepper.get(GregorianCalendar.YEAR), stepper.get(GregorianCalendar.MONTH) + 1, stepper.get(GregorianCalendar.DAY_OF_MONTH), start.get(GregorianCalendar.HOUR_OF_DAY), start.get(GregorianCalendar.MINUTE));
			} //exits with stepper in the same month same year as the end date
			accumulator += end.get(GregorianCalendar.DAY_OF_MONTH) + 1; //add an extra one to compensate for the indexing @ 0
			day = accumulator; //our previous day count was wrong, possibly even < 0
		}
	return day;
	}
	
//returns true if the current date and time is between two other days & times
	public boolean inBlackout(GregorianCalendar end, GregorianCalendar start)
	{
		GregorianCalendar now = new GregorianCalendar();
		if (now.after(start) && now.before(end))
		{
			return true;
		}
		return false;
	}
}
