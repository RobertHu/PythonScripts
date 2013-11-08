﻿using System;

namespace TradingConsole.Silverlight.Common
{
    public class TradeDay
    {
        public DateTime CurrentDay
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

        public DateTime LastDay
        {
            get;
            set;
        }
    }
}