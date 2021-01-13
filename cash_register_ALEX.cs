<Query Kind="Program" />

void Main()
{
	
	var cashInRegister = new CashRegister(0.01m);
	var change = cashInRegister.Checkout(100);
	Console.WriteLine(change);
}

public class CashRegister
{
	private readonly decimal _price;
	private readonly List<string> _change = new List<string>();

	public CashRegister(decimal price)
	{
		_price = price;
	}

	private static readonly IDictionary<decimal, string> CashInRegister = new Dictionary<decimal, string>()
	{
		{50m,"Fifty Pounds"},
		{20m,"Twenty Pounds"},
		{10m,"Ten Pounds"},
		{5m,"Five Pounds"},
		{2m,"Two Pounds"},
		{1m,"One Pound"},
		{0.5m,"Fifty Pence"},
		{0.2m,"Twenty Pence"},
		{0.1m,"Ten Pence"},
		{0.05m,"Five Pence"},
		{0.02m,"Two Pence"},
		{0.01m,"One Pence"},
	};

	public List<string> Checkout(decimal cash)
	{
		var changeOwed = cash - _price;
		
		if(changeOwed == 0)
		{
			return new List<string>{"ZERO"};
		}else if(changeOwed < 0)
		{
			return new List<string>{"ERROR"};
		}else
		{
			return CalculateChange(changeOwed);
		}
	}

	private List<string> CalculateChange(decimal cash)
	{
		var tender = CashInRegister.Keys.ToList();
		
		for(int i = 0; i<tender.Count(); i++)
		{
			if(cash - tender[i] >= 0)
			{
				CashInRegister.TryGetValue(tender[i], out var changeAsString);
				_change.Add(changeAsString);
				
				cash -= tender[i];
				i--;
			}
		}
		
		return _change;

	}

}
