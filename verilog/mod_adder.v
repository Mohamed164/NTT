module ModuloAdder #(parameter K = 8) (
    input  [K-1:0] A,   // K-bit positive integer A
    input  [K-1:0] B,   // K-bit positive integer B
    input  [K-1:0] M,   // K-bit positive integer M
    output reg [K-1:0] C // K-bit positive integer C
);
    
    wire [K:0] T1; // K+1 bits to avoid overflow
    wire [K:0] T2, T3;

    assign T1 = A + B;          // T1 = A + B
    assign T2 = T1 - M;         // T2 = T1 - M
    assign T3 = T1 - (2 * M);   // T3 = T1 - 2 * M

    always @(*) begin
        if (T2 < 0) begin
            C = T1[K-1:0]; // C = T1 if T2 < 0
        end else if (T3 < 0) begin
            C = T2[K-1:0]; // C = T2 if T3 < 0
        end else begin
            C = T3[K-1:0]; // C = T3 otherwise
        end
    end

endmodule
