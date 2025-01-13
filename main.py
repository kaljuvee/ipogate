from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    styles = """
        .hero {
            text-align: center;
            padding: 4rem 2rem;
            background: #f5f5f5;
        }

        .features, .additional-tools, .why-choose-us {
            padding: 2rem;
        }

        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .button.primary {
            display: inline-block;
            padding: 0.8rem 1.6rem;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 1rem 0;
        }

        .button.primary:hover {
            background: #0056b3;
        }

        .text-center {
            text-align: center;
        }
    """
    
    return Titled(
        "IPOLabs - Your Gateway to Public Markets",
        styles=styles,
        content=Main(
            # Hero section
            Section(cls="hero",
                H1("IPOLabs"),
                H2("Your Gateway to Public Markets"),
                P("IPOGate guides you through every step of your IPO journey with our AI-powered tools and analytics."),
                A("Begin Your IPO Journey", href="/document-analysis", cls="button primary")
            ),

            # Main features section
            Section(cls="features",
                H2("Your Path to Going Public"),
                
                Article(
                    H3("1. Document Analysis 📄"),
                    P("Transform your company documents into a professional prospectus:"),
                    Ul(
                        Li("Upload your company documents (PDF, DOCX, or TXT)"),
                        Li("AI-powered extraction of key company information"),
                        Li("Automated prospectus generation with standardized formatting"),
                        Li("Review and edit capabilities for accuracy")
                    )
                ),

                Article(
                    H3("2. Multiplier Valuation 📊"),
                    P("Determine your company's market value using industry standards:"),
                    Ul(
                        Li("Industry-specific multiple analysis"),
                        Li("Peer comparison metrics"),
                        Li("Automated valuation calculations"),
                        Li("Customizable parameters for precise estimates")
                    )
                ),

                Article(
                    H3("3. Comparative Analysis 📈"),
                    P("Benchmark your company against industry peers:"),
                    Ul(
                        Li("Comprehensive peer group analysis"),
                        Li("Market positioning assessment"),
                        Li("Competitive advantage evaluation"),
                        Li("Growth potential analysis")
                    )
                )
            ),

            # Additional tools section
            Section(cls="additional-tools",
                H2("Additional Tools & Resources"),
                
                Div(cls="tools-grid",
                    Article(
                        H3("Financial Analysis"),
                        Ul(
                            Li("Detailed financial statement analysis"),
                            Li("Key performance indicators"),
                            Li("Growth projections"),
                            Li("Cash flow analysis")
                        )
                    ),
                    
                    Article(
                        H3("Risk Assessment"),
                        Ul(
                            Li("Industry-specific risk factors"),
                            Li("Market condition analysis"),
                            Li("Regulatory compliance checks"),
                            Li("Mitigation strategies")
                        )
                    ),
                    
                    Article(
                        H3("Market Intelligence"),
                        Ul(
                            Li("Industry trends and insights"),
                            Li("Market sentiment analysis"),
                            Li("Investor preference tracking"),
                            Li("Timing recommendations")
                        )
                    )
                )
            ),

            # Why choose us section
            Section(cls="why-choose-us",
                H2("Why Choose IPOLabs?"),
                Ul(
                    Li(Strong("AI-Powered Analysis"), ": Advanced algorithms for accurate data extraction and analysis"),
                    Li(Strong("Time Efficiency"), ": Automate manual processes and focus on strategic decisions"),
                    Li(Strong("Professional Output"), ": Generate investor-ready documents and presentations"),
                    Li(Strong("Expert Guidance"), ": Step-by-step assistance throughout your IPO journey")
                ),
                P(
                    "Ready to take your company public? ",
                    A("Begin Your IPO Journey", href="/document-analysis", cls="button primary")
                )
            ),

            # Footer
            Footer(
                Hr(),
                P(
                    "For more information about our services, please visit our ",
                    A("About Us", href="/about"),
                    " page or contact our team.",
                    cls="text-center"
                )
            )
        )
    )

if __name__ == "__main__":
    serve() 