import java.util.GregorianCalendar;

public class TemporalManager 
{
	public TemporalManager()
	{
		
	}
//returns year, month, dayOfMonth, hourOfDay, minute
	
//returns the number of days between end and start dates
	public int Daysdifference(GregorianCalendar start, GregorianCalendar end)
	{
		String temp = "";
		int year = end.get(GregorianCalendar.YEAR) - start.get(GregorianCalendar.YEAR); //this should never be negative, if it is there is an error
		int month = end.get(GregorianCalendar.MONTH) - start.get(GregorianCalendar.MONTH);
		if (month < 0)
		{
			year = year -1; 
			month = month + 12;
			//i.e. November 1 2016 start to January 1 2017 end would have year = 1, month = (0-10) = -10, 
			//adjust by adding 12 to see 2 months (November, December) difference between the two dates
		}
		int day = end.get(GregorianCalendar.DAY_OF_MONTH) - start.get(GregorianCalendar.DAY_OF_MONTH);
		if(day == 0 && month > 0) //if there is some difference between them
		{
			GregorianCalendar stepper = start;
			for (int i = stepper.get(GregorianCalendar.MONTH); i < stepper.get(GregorianCalendar.MONTH) + month; i++)
			{
				day += stepper.getActualMaximum(GregorianCalendar.DAY_OF_MONTH);
				GregorianCalendar temp_cal = new GregorianCalendar(stepper.get(GregorianCalendar.YEAR), i, stepper.get(GregorianCalendar.DAY_OF_MONTH), stepper.get(GregorianCalendar.HOUR_OF_DAY), stepper.get(GregorianCalendar.MINUTE));
				stepper = temp_cal;
			}
			month = 0; //we have now accounted for the # days between the two dates
		}
		else if (day < 0)
		{
			day = start.getActualMaximum(GregorianCalendar.DAY_OF_MONTH) - start.get(GregorianCalendar.DAY_OF_MONTH);
			day += end.get(GregorianCalendar.DAY_OF_MONTH);
			month --;
		}
		
		if (month > 0){
			GregorianCalendar stepper = new GregorianCalendar(start.get(GregorianCalendar.YEAR), start.get(GregorianCalendar.MONTH) + 1, start.get(GregorianCalendar.DAY_OF_MONTH), start.get(GregorianCalendar.HOUR_OF_DAY), start.get(GregorianCalendar.MINUTE));
			for (int i = stepper.get(GregorianCalendar.MONTH); i < stepper.get(GregorianCalendar.MONTH) + month; i++)
			{
				day += stepper.getActualMaximum(GregorianCalendar.DAY_OF_MONTH);
				GregorianCalendar temp_cal = new GregorianCalendar(stepper.get(GregorianCalendar.YEAR), i, stepper.get(GregorianCalendar.DAY_OF_MONTH), stepper.get(GregorianCalendar.HOUR_OF_DAY), stepper.get(GregorianCalendar.MINUTE));
				stepper = temp_cal;
			}
			month = 0; //we have now accounted for the # days between the two dates
		}
		return day;

	}
}
