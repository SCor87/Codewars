/*
    DESCRIPTION:

    Write a function which calculates the average of the numbers in a given array.
    Note: Empty arrays should return 0.
*/
//My solution

class AverageSolution
{
    public static double FindAverage(double[] array)
    {
        double sum = 0, average = 0, length = array.Length;
      
        foreach(double num in array)
        {
          sum += num;
        }
      
        average = sum / length;
      
        return average;
    }
} 