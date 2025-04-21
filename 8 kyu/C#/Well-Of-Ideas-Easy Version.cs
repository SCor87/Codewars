/*
    DESCRIPTION:

    For every good kata idea there seem to be quite a few bad ones!

    In this kata you need to check the provided array (x) for good ideas 'good' and 
    bad ideas 'bad'.   
    If there are one or two good ideas, return 'Publish!', if there are more than 
    2 return 'I smell a series!'. If there are no good ideas, as is often the 
    case, return 'Fail!'.
*/

//My solution

using System.Linq;
public class Kata
{
  public static string Well(string[] x)
  {
     int wordCount = x.Count(i => i== "good"); //counting arr x for str "good" assigning it to int type variable
    
    if (wordCount == 0) //beginning of if, else-if statement to check for value of wordCount variable
      {
      return "Fail!";
    }
    else if(wordCount <= 2)
      {
      return "Publish!";
    }
    else
      {
      return "I smell a series!";
    }
  }
}