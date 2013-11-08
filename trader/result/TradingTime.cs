﻿using System;

namespace TradingConsole.Silverlight.Common
{
    public class TradingTime
    {
        public Guid InstrumentId
        {
            get;
            set;
        }

        public DateTime BeginTime
        {
            get;
            set;
        }

        public DateTime EndTime
        {
            get;
            set;
        }
    }
}