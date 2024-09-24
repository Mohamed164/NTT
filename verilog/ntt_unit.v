module NTT_Unit(
    input [31:0] W,       // Twiddle factor
    input [31:0] Left,    // Left input
    input [31:0] Right,   // Right input
    input [31:0] q,       // Modulus q
    output [31:0] Odd,    // Odd output
    output [31:0] Even    // Even output
);

    wire [31:0] mod_sum, mod_diff, mod_prod;
    wire [63:0] prod_full;
    wire [31:0] prod;

    // Instantiate Modular Adder: (Left + Right) % q
    ModularAdder mod_add_inst (
        .a(Left),
        .b(Right),
        .modulus(q),
        .result(mod_sum)
    );
    
    // Instantiate Modular Subtractor: (Left - Right) % q
    ModularSubtractor mod_sub_inst (
        .a(Left),
        .b(Right),
        .modulus(q),
        .result(mod_diff)
    );
    
    // 32x32 multiplier: W * mod_diff
    assign prod_full = W * mod_diff;  // Full 64-bit product
    assign prod = prod_full[31:0];    // Keep lower 32 bits of product
    
    // Instantiate Modular Reduction: (W * mod_diff) % q
    ModularReduction mod_red_inst (
        .a(prod),
        .modulus(q),
        .result(mod_prod)
    );
    
    // Outputs
    assign Even = mod_sum;  // Output from Modular Adder
    assign Odd = mod_prod;  // Output from Modular Reduction

endmodule
