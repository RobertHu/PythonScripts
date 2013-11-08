using System;

namespace TradingConsole.Silverlight.Common
{
    public class Currency
    {
        public Guid Id
        {
            get;
            set;
        }

        public string Code
        {
            get;
            set;
        }

        public int Decimals
        {
            get;
            set;
        }

        public decimal? MinDeposit
        {
            get;
            set;
        }

        public string Name
        {
            get;
            set;
        }

        public string Alias
        {
            get;
            set;
        }
    }
}