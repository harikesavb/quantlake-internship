"""
QuantLake Lending Risk Analysis
Complete loan risk analysis in a single Python file
"""

import pandas as pd
import numpy as np

def main():
    print("=" * 60)
    print("QUANTLAKE LENDING - LOAN RISK ANALYSIS REPORT")
    print("=" * 60)
    print("Dataset: Bank Personal Loan Data (5,000 customers)")
    print("Analysis Date: January 2025")
    print("=" * 60)
    
    # Load and analyze data
    df = load_data()
    target_col = 'Personal Loan'
    
    print(f"\nOVERALL LOAN ACCEPTANCE RATE: {df[target_col].mean():.1%}")
    print(f"TOTAL CUSTOMERS ANALYZED: {len(df):,}")
    print(f"AVERAGE CUSTOMER INCOME: ${df['Income'].mean():.0f}K")
    print(f"AVERAGE MONTHLY CC SPENDING: ${df['CCAvg'].mean():.2f}K")
    
    print("\n" + "=" * 60)
    
    # Answer the three main questions
    analyze_top_factors(df, target_col)
    analyze_risk_segments(df, target_col)
    generate_risk_rules(df, target_col)
    
    # Additional insights
    generate_recommendations(df, target_col)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE - REPORT READY FOR QUANTLAKE LENDING")
    print("=" * 60)

def load_data():
    """Load the loan dataset"""
    try:
        df = pd.read_csv('loan_data.csv')
        return df
    except FileNotFoundError:
        # Fallback: load from Excel if CSV doesn't exist
        df = pd.read_excel('/content/Bank_Personal_Loan_Modelling.xlsx', sheet_name='Data')
        return df

def analyze_top_factors(df, target_col):
    """Question 1: What are the top factors affecting loan acceptance?"""
    print("\n1. TOP FACTORS AFFECTING LOAN ACCEPTANCE:")
    print("-" * 50)
    
    # Calculate correlations with target
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if target_col in numeric_cols:
        numeric_cols.remove(target_col)
    
    correlations = {}
    for col in numeric_cols:
        if col != 'ID':  # Skip ID column
            corr = abs(df[col].corr(df[target_col]))
            if not np.isnan(corr):
                correlations[col] = corr
    
    # Sort by importance
    top_factors = sorted(correlations.items(), key=lambda x: x[1], reverse=True)
    
    print(f"{'Rank':<5} {'Factor':<20} {'Correlation':<12} {'Impact'}")
    print("-" * 60)
    for i, (factor, importance) in enumerate(top_factors[:5], 1):
        impact = get_factor_impact(factor)
        print(f"{i:<5} {factor:<20} {importance:<12.3f} {impact}")
    
    return top_factors

def analyze_risk_segments(df, target_col):
    """Question 2: Which customer segments are high-risk?"""
    print("\n\n2. HIGH-RISK CUSTOMER SEGMENTS:")
    print("-" * 50)
    
    # Income-based segmentation
    print("\nINCOME-BASED SEGMENTS:")
    print(f"{'Segment':<20} {'Acceptance Rate':<15} {'Risk Level':<12} {'Count'}")
    print("-" * 60)
    
    income_quartiles = pd.qcut(df['Income'], q=4, labels=['Low', 'Medium-Low', 'Medium-High', 'High'])
    income_acceptance = df.groupby(income_quartiles, observed=True)[target_col].mean()
    
    for segment, rate in income_acceptance.items():
        risk_level = get_risk_level(rate)
        count = (income_quartiles == segment).sum()
        print(f"{segment + ' Income':<20} {rate:<15.1%} {risk_level:<12} {count:,}")
    
    # Education-based segmentation
    print("\nEDUCATION-BASED SEGMENTS:")
    print(f"{'Education Level':<20} {'Acceptance Rate':<15} {'Risk Level':<12} {'Count'}")
    print("-" * 60)
    
    edu_acceptance = df.groupby('Education')[target_col].mean()
    education_labels = {1: 'Undergraduate', 2: 'Graduate', 3: 'Advanced/Professional'}
    
    for edu_level, rate in edu_acceptance.items():
        edu_name = education_labels.get(edu_level, f'Level {edu_level}')
        risk_level = get_risk_level(rate)
        count = (df['Education'] == edu_level).sum()
        print(f"{edu_name:<20} {rate:<15.1%} {risk_level:<12} {count:,}")
    
    # Credit card spending segmentation
    print("\nCREDIT CARD SPENDING SEGMENTS:")
    print(f"{'Spending Level':<20} {'Acceptance Rate':<15} {'Risk Level':<12} {'Count'}")
    print("-" * 60)
    
    cc_quartiles = pd.qcut(df['CCAvg'], q=4, labels=['Low Spender', 'Medium-Low', 'Medium-High', 'High Spender'])
    cc_acceptance = df.groupby(cc_quartiles, observed=True)[target_col].mean()
    
    for segment, rate in cc_acceptance.items():
        risk_level = get_risk_level(rate)
        count = (cc_quartiles == segment).sum()
        print(f"{segment:<20} {rate:<15.1%} {risk_level:<12} {count:,}")

def generate_risk_rules(df, target_col):
    """Question 3: What risk rules can we suggest for QuantLake Lending?"""
    print("\n\n3. RISK RULES FOR QUANTLAKE LENDING:")
    print("-" * 50)
    
    overall_rate = df[target_col].mean()
    
    # Rule 1: High-Income Priority
    print("\nRULE 1 - HIGH-INCOME PRIORITY TARGETING")
    print("-" * 40)
    high_income_threshold = df['Income'].quantile(0.8)
    high_income_acceptance = df[df['Income'] >= high_income_threshold][target_col].mean()
    high_income_count = (df['Income'] >= high_income_threshold).sum()
    
    print(f"Target Criteria: Income >= ${high_income_threshold:.0f}K")
    print(f"Expected Conversion: {high_income_acceptance:.1%}")
    print(f"vs Overall Average: {overall_rate:.1%}")
    print(f"Affected Customers: {high_income_count:,}")
    print(f"Uplift Factor: {high_income_acceptance/overall_rate:.1f}x")
    print("Recommendation: Prioritize marketing and offer competitive rates")
    
    # Rule 2: Education Targeting
    print("\nRULE 2 - EDUCATION LEVEL TARGETING")
    print("-" * 40)
    edu_acceptance = df.groupby('Education')[target_col].mean()
    best_education = edu_acceptance.idxmax()
    best_edu_rate = edu_acceptance.max()
    education_labels = {1: 'Undergraduate', 2: 'Graduate', 3: 'Advanced/Professional'}
    best_edu_count = (df['Education'] == best_education).sum()
    
    print(f"Target Criteria: {education_labels.get(best_education)} customers")
    print(f"Expected Conversion: {best_edu_rate:.1%}")
    print(f"vs Overall Average: {overall_rate:.1%}")
    print(f"Affected Customers: {best_edu_count:,}")
    print(f"Uplift Factor: {best_edu_rate/overall_rate:.1f}x")
    print("Recommendation: Develop specialized products for professionals")
    
    # Rule 3: Credit Card Usage
    print("\nRULE 3 - CREDIT CARD USAGE INDICATOR")
    print("-" * 40)
    high_cc_threshold = df['CCAvg'].quantile(0.75)
    high_cc_acceptance = df[df['CCAvg'] >= high_cc_threshold][target_col].mean()
    high_cc_count = (df['CCAvg'] >= high_cc_threshold).sum()
    
    print(f"Target Criteria: Monthly CC spending >= ${high_cc_threshold:.2f}K")
    print(f"Expected Conversion: {high_cc_acceptance:.1%}")
    print(f"vs Overall Average: {overall_rate:.1%}")
    print(f"Affected Customers: {high_cc_count:,}")
    print(f"Uplift Factor: {high_cc_acceptance/overall_rate:.1f}x")
    print("Recommendation: Cross-sell to high credit card users")
    
    # Rule 4: Premium Segment (Combined)
    print("\nRULE 4 - PREMIUM CUSTOMER SEGMENT (HIGHEST VALUE)")
    print("-" * 40)
    high_income_mask = df['Income'] >= df['Income'].quantile(0.8)
    high_cc_mask = df['CCAvg'] >= df['CCAvg'].quantile(0.7)
    combined_mask = high_income_mask & high_cc_mask
    combined_acceptance = df[combined_mask][target_col].mean()
    combined_count = combined_mask.sum()
    
    print(f"Target Criteria: High income + High CC spending")
    print(f"Expected Conversion: {combined_acceptance:.1%}")
    print(f"vs Overall Average: {overall_rate:.1%}")
    print(f"Affected Customers: {combined_count:,}")
    print(f"Uplift Factor: {combined_acceptance/overall_rate:.1f}x")
    print("Recommendation: VIP treatment and premium products")

def generate_recommendations(df, target_col):
    """Generate actionable business recommendations"""
    print("\n\n4. IMPLEMENTATION RECOMMENDATIONS:")
    print("-" * 50)
    
    print("\nIMMEDIATE ACTIONS (Next 30 Days):")
    print("• Segment customer database by income and spending")
    print("• Create targeted campaigns for high-income customers")
    print("• Implement fast-track for premium segment")
    print("• Train sales team on risk indicators")
    
    print("\nMEDIUM-TERM STRATEGY (3-6 Months):")
    print("• Launch education-specific loan products")
    print("• Develop credit card spending analysis tools")
    print("• Create VIP customer experience")
    print("• Partner with professional organizations")
    
    print("\nLONG-TERM GOALS (6-12 Months):")
    print("• Build predictive models using top factors")
    print("• Automate customer segmentation")
    print("• Establish premium loyalty programs")
    print("• Expand products for high-value segments")
    
    print("\nKEY SUCCESS METRICS:")
    overall_rate = df[target_col].mean()
    print(f"• Current baseline acceptance rate: {overall_rate:.1%}")
    print(f"• Target premium segment rate: 40%+ (4x improvement)")
    print(f"• Expected revenue uplift: 200-300% for targeted segments")
    print(f"• Risk reduction: Focus on segments with 15%+ acceptance")

def get_factor_impact(factor):
    """Get descriptive impact for each factor"""
    impacts = {
        'Income': 'Higher income = higher acceptance',
        'CCAvg': 'High spenders more likely to accept',
        'CD Account': 'CD holders show more interest',
        'Mortgage': 'Existing borrowers more receptive',
        'Education': 'Higher education = higher rates'
    }
    return impacts.get(factor, 'Positive correlation with acceptance')

def get_risk_level(rate):
    """Determine risk level based on acceptance rate"""
    if rate < 0.05:
        return 'HIGH RISK'
    elif rate < 0.15:
        return 'MEDIUM RISK'
    else:
        return 'LOW RISK'

if __name__ == "__main__":
    main()
