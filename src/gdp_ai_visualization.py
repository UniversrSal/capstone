import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_gdp_ai_comparison():
    """
    Creates a side-by-side visualization comparing GDP output and AI focus
    between United States and Israel.
    
    Returns:
        fig: matplotlib figure object
    """
    # Create figure with 2 subplots (1 bar chart, 1 pie chart)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # ============= CHART 1: GDP OUTPUT BY COUNTRY =============
    countries = ['United States', 'Israel']
    gdp_values = [29184900000000, 540381000000]  # USD
    colors = ['#E63946', '#457B9D']  # Red for USA, Blue for Israel

    bars = ax1.bar(countries, gdp_values, color=colors, edgecolor='black', linewidth=2, alpha=0.85)

    # Format y-axis with trillion/billion labels
    ax1.set_ylabel('GDP (USD)', fontsize=12, fontweight='bold')
    ax1.set_title('National Economic Output (2024)', 
                  fontsize=14, fontweight='bold', pad=20)
    ax1.set_ylim(0, gdp_values[0] * 1.1)

    # Add value labels on bars
    for bar, value in zip(bars, gdp_values):
        height = bar.get_height()
        if value >= 1e12:
            label_text = f'${value/1e12:.2f}T'
        else:
            label_text = f'${value/1e9:.1f}B'
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                label_text, ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Format y-axis ticks
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e12:.1f}T' if x >= 1e12 else f'${x/1e9:.0f}B'))
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # ============= CHART 2: COUNTRY AI FOCUS (PIE CHART) =============
    focus_countries = ['United States', 'Israel']
    focus_values = [65, 35]  # USA 65%, Israel 35%
    
    wedges, texts, autotexts = ax2.pie(focus_values, 
                                         labels=focus_countries, 
                                         autopct='%1.1f%%',
                                         colors=colors,
                                         startangle=90,
                                         textprops={'fontsize': 12, 'fontweight': 'bold'},
                                         explode=(0.05, 0.05))

    ax2.set_title('AI Investment Focus Distribution', 
                  fontsize=14, fontweight='bold', pad=20)

    # Format percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize=11
        autotext.set_fontweight('bold')

    # ============= LAYOUT & STYLING =============
    fig.suptitle('USA vs Israel: Economic Output & AI Investment Focus (2024-2025)', 
                 fontsize=16, fontweight='bold', y=0.98)

    plt.tight_layout()
    
    return fig


def print_analysis_summary():
    """
    Prints a detailed summary table of GDP and AI investment comparison.
    """
    print("\n" + "="*100)
    print("GDP & AI INVESTMENT CORRELATION ANALYSIS: USA vs ISRAEL")
    print("="*100)

    summary_data = {
        'Metric': [
            'GDP 2024 (USD)',
            'AI Spending 2025 (USD)',
            'AI as % of GDP',
            'GDP per Capita',
            'AI Spending per Capita',
            'Primary AI Focus',
            'Investment Strategy'
        ],
        'United States': [
            '$29.18 Trillion',
            '$470.9 Billion',
            '1.61%',
            '$87,000',
            '$1,420',
            'Generative AI, Enterprise Automation, Infrastructure',
            'Breadth & Scale - Maximize adoption across all sectors'
        ],
        'Israel': [
            '$540.38 Billion',
            '$15 Billion',
            '2.78%',
            '$94,805',
            '$2,632',
            'Cybersecurity, Defense, Startup Ecosystem',
            'Depth & Specialization - High-value specialized applications'
        ]
    }

    summary_df = pd.DataFrame(summary_data)
    print(summary_df.to_string(index=False))
    print("="*100)
    print("\nKEY FINDINGS:")
    print("  • USA economy is 54x larger than Israel's")
    print("  • Israel invests 1.85x MORE per capita than USA ($2,632 vs $1,420)")
    print("  • Israel dedicates a higher % of GDP to AI (2.78% vs 1.61%)")
    print("  • USA focuses on breadth: spreading AI across industries")
    print("  • Israel focuses on depth: specialized excellence in niche domains")
    print("="*100 + "\n")


if __name__ == "__main__":
    # Generate the visualization
    fig = create_gdp_ai_comparison()
    
    # Print analysis summary
    print_analysis_summary()
    
    # Save figure
    plt.savefig('gdp_ai_comparison.png', dpi=300, bbox_inches='tight')
    print("✓ Chart saved as 'gdp_ai_comparison.png'")
    plt.show()
