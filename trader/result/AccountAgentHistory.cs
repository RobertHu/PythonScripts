using System;

namespace TradingConsole.Silverlight.Common
{
    public class AccountAgentHistory
    {
        public Guid AccountId
        {
            get;
            set;
        }

        public Guid AgentAccountId
        {
            get;
            set;
        }

        public DateTime AgentBeginTime
        {
            get;
            set;
        }

        public DateTime AgentEndTime
        {
            get;
            set;
        }
    }
}