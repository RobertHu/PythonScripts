using System;

namespace TradingConsole.Silverlight.Common
{
    public class QuotePolicyDetail
    {
        public Guid QuotePolicyId
        {
            get;
            set;
        }

        public Guid InstrumentId
        {
            get;
            set;
        }

        public bool IsOriginHiLo
        {
            get;
            set;
        }

        public int HiLoSpread
        {
            get;
            set;
        }

        public int Spread
        {
            get;
            set;
        }
    }
}