/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let idxLeft = 0;
    let idxRight = 1;
    let maxProfit = 0;

    while(idxRight < prices.length) {
        if (prices[idxRight] <= prices[idxLeft]) {
            idxLeft = idxRight;
        }

        const profit = prices[idxRight] - prices[idxLeft];

        maxProfit = Math.max(maxProfit, profit);
        idxRight++;
    }
    return maxProfit;
};