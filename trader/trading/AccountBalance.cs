using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Trader.Server.CppTrader.DataMapping
{
    public class ResetAccount
    {
        public Guid Account { get; set; }
        public Common.AccountBalance AccountBalance { get; set; }
        public Common.AccountCurrency[] AccountCurrencies { get; set; }
        public Common.Transaction[] Transactions { get; set; }
        public Common.Order[] Orders { get; set; }
        public Common.Contract[] Contracts { get; set; }
        public Common.OrderRelation[] OrderRelations { get; set; }

        public override string ToString()
        {
            StringBuilder stringBuilder = new StringBuilder();

            if (Account != null)
            {
                stringBuilder.Append("Account=");
                stringBuilder.Append(Account);
                stringBuilder.Append(";");
            }

            if (AccountBalance != null)
            {
                stringBuilder.Append("AccountBalance=");
                stringBuilder.Append(AccountBalance);
                stringBuilder.Append(";");
            }

            if (AccountCurrencies != null && AccountCurrencies.Length > 0)
            {
                stringBuilder.Append("AccountCurrencies:");
                foreach (Common.AccountCurrency accountCurrency in AccountCurrencies)
                {
                    stringBuilder.Append(accountCurrency);
                    stringBuilder.Append(";");
                }
                stringBuilder.Append("\t");
            }

            if (Transactions != null && Transactions.Length > 0)
            {
                stringBuilder.Append("Transactions:");
                foreach (Common.Transaction transaction in Transactions)
                {
                    stringBuilder.Append(transaction);
                    stringBuilder.Append(";");
                }
                stringBuilder.Append("\t");
            }

            if (Orders != null && Orders.Length > 0)
            {
                stringBuilder.Append("Orders:");
                foreach (Common.Order order in Orders)
                {
                    stringBuilder.Append(order);
                    stringBuilder.Append(";");
                }
                stringBuilder.Append("\t");
            }

            if (Contracts != null && Contracts.Length > 0)
            {
                stringBuilder.Append("Contracts:");
                foreach (Common.Contract contract in Contracts)
                {
                    stringBuilder.Append(contract);
                    stringBuilder.Append(";");
                }
                stringBuilder.Append("\t");
            }

            if (OrderRelations != null && OrderRelations.Length > 0)
            {
                stringBuilder.Append("OrderRelations:");
                foreach (Common.OrderRelation orderRelation in OrderRelations)
                {
                    stringBuilder.Append(orderRelation);
                    stringBuilder.Append(";");
                }
            }

            return stringBuilder.ToString();
        }
    }

    public class AccountBalance
    {
        public Guid AccountId{ get; set; }

        public Guid? CurrencyId { get; set; }

        public decimal? Balance{ get; set; }

        public decimal? Necessary{ get; set; }

        public decimal? PedgeAmount { get; set; }

        public decimal? FrozenFund { get; set; }
        
        public decimal? InterestPLNotValued{ get; set; }

        public decimal? StoragePLNotValued{ get; set; }

        public decimal? TradePLNotValued{ get; set; }

        public decimal? InterestPLFloat{ get; set; }

        public decimal? StoragePLFloat{ get; set; }

        public decimal? TradePLFloat{ get; set; }

        public AlertLevel AlertLevel{ get; set; }

        public decimal? UnclearAmount { get; set; }

        public UpdateAction UpdateAction { get; set; }

        public override string ToString()
        {
            return string.Format("AccountId={0}, CurrencyId={1}, Balance={2}, Necessary={3}, InterestPLNotValued={4}, StoragePLNotValued={5}, TradePLNotValued={6}, InterestPLFloat={7}, StoragePLFloat={8}, TradePLFloat={9}, AlertLevel={10}, UnclearAmount={11}, UpdateAction={12}, PedgeAmount={13}, FrozenFund={14}",
                AccountId, CurrencyId == null ? "NULL" : CurrencyId.ToString(), Balance, Necessary, InterestPLNotValued, StoragePLNotValued, TradePLNotValued, InterestPLFloat, StoragePLFloat, TradePLFloat, AlertLevel, UnclearAmount, UpdateAction, PedgeAmount, FrozenFund);
        }
    }
}