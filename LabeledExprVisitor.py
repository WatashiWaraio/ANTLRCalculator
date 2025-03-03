# Generated from LabeledExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LabeledExprParser import LabeledExprParser
else:
    from LabeledExprParser import LabeledExprParser

# This class defines a complete generic visitor for a parse tree produced by LabeledExprParser.

class LabeledExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LabeledExprParser#prog.
    def visitProg(self, ctx:LabeledExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#printExpr.
    def visitPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#assign.
    def visitAssign(self, ctx:LabeledExprParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#blank.
    def visitBlank(self, ctx:LabeledExprParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#tan.
    def visitTan(self, ctx:LabeledExprParser.TanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#parens.
    def visitParens(self, ctx:LabeledExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#MulDiv.
    def visitMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#AddSub.
    def visitAddSub(self, ctx:LabeledExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#cos.
    def visitCos(self, ctx:LabeledExprParser.CosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#Sqrt.
    def visitSqrt(self, ctx:LabeledExprParser.SqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#sin.
    def visitSin(self, ctx:LabeledExprParser.SinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#Pow.
    def visitPow(self, ctx:LabeledExprParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#id.
    def visitId(self, ctx:LabeledExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#log3.
    def visitLog3(self, ctx:LabeledExprParser.Log3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#int.
    def visitInt(self, ctx:LabeledExprParser.IntContext):
        return self.visitChildren(ctx)



del LabeledExprParser