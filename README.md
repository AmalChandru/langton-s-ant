# langton-s-ant
# Implementation of a two-dimensional universal Turing machine invented by Chris Langton.
Squares on a plane are colored variously either black or white. We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:

1) If the ant is on a black square, it turns right 90 degrees and moves forward one unit.
2) If the ant is on a white square, it turns left 90 degrees and moves forward one unit.
3) When the ant leaves a square, it inverts the color.


We can extend this to multiple states (Semi-chaotic, Spiral..), multiple colors (LLRR, R1R2NUR2R1L2....)

I came to know about this by [Numberphile!](https://www.youtube.com/watch?v=NWBToaXK5T0)
# Resources
1) -->[Wikipedia](https://en.wikipedia.org/wiki/Langton%27s_ant)


2) -->[Simulation](http://www.langtonant.com/)

3) -->[Implementation](https://rosettacode.org/wiki/Langton%27s_ant)
