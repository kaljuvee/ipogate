import streamlit as st
from ai.analysis_agent import CompanyAnalysisAgent
import yaml
import os
from dotenv import load_dotenv
import pdfkit
import tempfile
from datetime import datetime
from markdown import markdown
import base64
import json

def json_to_markdown(data):
    """Convert JSON data to formatted markdown"""
    md = "# Company Prospectus\n\n"
    md += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # Basic Information
    if 'basic_information' in data:
        md += "## Basic Information\n\n"
        for key, value in data['basic_information'].items():
            key = key.replace('-_', '').replace('_', ' ').title()
            md += f"**{key}**: {value}\n\n"
    
    # Share Offering Details
    if 'share_offering_details' in data:
        md += "## Share Offering Details\n\n"
        for key, value in data['share_offering_details'].items():
            key = key.replace('-_', '').replace('_', ' ').title()
            md += f"**{key}**: {value}\n\n"
    
    # Company Overview
    if 'company_overview' in data:
        md += "## Company Overview\n\n"
        for key, value in data['company_overview'].items():
            key = key.replace('-_', '').replace('_', ' ').title()
            md += f"**{key}**: {value}\n\n"
    
    # Management Structure
    if 'management_structure' in data:
        md += "## Management Structure\n\n"
        for key, value in data['management_structure'].items():
            key = key.replace('-_', '').replace('_', ' ').title()
            md += f"**{key}**: {value}\n\n"
    
    # Financial Information
    if 'financial_information' in data:
        md += "## Financial Information\n\n"
        for key, value in data['financial_information'].items():
            key = key.replace('-_', '').replace('_', ' ').title()
            md += f"**{key}**: {value}\n\n"
    
    # Market Analysis
    if 'market_analysis' in data:
        md += "## Market Analysis\n\n"
        for key, value in data['market_analysis'].items():
            key = key.replace('-_', '').replace('_', ' ').title()
            md += f"**{key}**: {value}\n\n"
    
    # Risk Factors
    if 'risk_factors' in data:
        md += "## Risk Factors\n\n"
        for key, value in data['risk_factors'].items():
            key = key.replace('-_', '').replace('_', ' ').title()
            md += f"**{key}**: {value}\n\n"
    
    # Future Plans
    if 'future_plans' in data:
        md += "## Future Plans\n\n"
        for key, value in data['future_plans'].items():
            key = key.replace('-_', '').replace('_', ' ').title()
            md += f"**{key}**: {value}\n\n"
            
    return md

def save_json(data, company_name):
    """Save JSON data to data folder"""
    # Create data directory if it doesn't exist
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Create filename with timestamp and company name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    safe_company_name = ''.join(c for c in company_name if c.isalnum() or c in (' ', '-', '_')).strip()
    filename = f"{safe_company_name}_{timestamp}.json"
    
    filepath = os.path.join(data_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return filepath

# Load environment variables
load_dotenv()

st.title('IPOGate')
st.subheader('Your Gateway to Public Markets')

# Initialize session state
if 'extracted_data' not in st.session_state:
    st.session_state.extracted_data = None
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'selected_model' not in st.session_state:
    st.session_state.selected_model = "gpt-4o"
if 'show_editable' not in st.session_state:
    st.session_state.show_editable = False
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False

# Add model selection to sidebar
with st.sidebar:
    st.header("Settings")
    model_name = st.selectbox(
        "Select AI Model",
        options=["gpt-4o", "gpt-4o-mini"],
        help="Choose the OpenAI model to use for analysis",
        key='selected_model'
    )

# File upload section
uploaded_file = st.file_uploader("Upload company document (PDF, DOCX, or TXT)", 
                               type=['pdf', 'docx', 'txt'])

if uploaded_file and uploaded_file != st.session_state.uploaded_file:
    st.session_state.uploaded_file = uploaded_file
    st.session_state.analysis_complete = False
    st.session_state.show_editable = False

# Analysis button
if st.session_state.uploaded_file and not st.session_state.analysis_complete:
    if st.button('Analyze Document'):
        with st.spinner('Analyzing document...'):
            try:
                analysis_agent = CompanyAnalysisAgent(model_name=st.session_state.selected_model)
                extracted_data, debug_info = analysis_agent.analyze_document(st.session_state.uploaded_file)
                st.session_state.extracted_data = extracted_data
                st.session_state.debug_info = debug_info
                st.session_state.analysis_complete = True
                st.success('Document analyzed successfully!')
            except Exception as e:
                st.error(f'Error analyzing document: {str(e)}')

# Show analysis results
if st.session_state.analysis_complete and not st.session_state.show_editable:
    st.subheader("Analysis Results")
    st.json(st.session_state.extracted_data)
    
    if st.button('Proceed to Edit Information'):
        st.session_state.show_editable = True

# Edit form
if st.session_state.show_editable:
    with st.form("edit_form"):
        st.subheader("Company Details")
        st.write("Please review and edit the extracted information:")
        
        data = st.session_state.extracted_data
        
        # Basic Information
        with st.expander("Basic Information", expanded=True):
            basic_info = data.get('basic_information', {})
            company_name = st.text_input(
                "Company Name", 
                value=basic_info.get('-_company_name', '')
            )
            company_type = st.text_input(
                "Company Type", 
                value=basic_info.get('-_company_type', '')
            )
            jurisdiction = st.text_input(
                "Jurisdiction", 
                value=basic_info.get('-_jurisdiction', '')
            )
            
        # Share Offering Details
        with st.expander("Share Offering Details"):
            share_info = data.get('share_offering_details', {})
            num_shares = st.text_input(
                "Number of Shares", 
                value=share_info.get('-_number_of_shares', '')
            )
            nominal_value = st.text_input(
                "Nominal Value per Share", 
                value=share_info.get('-_nominal_value_per_share', '')
            )
            
        # Company Overview
        with st.expander("Company Overview"):
            overview = data.get('company_overview', {})
            founding_story = st.text_area(
                "Founding Story", 
                value=overview.get('-_founding_story', '')
            )
            core_business = st.text_area(
                "Core Business", 
                value=overview.get('-_core_business_description', '')
            )
            
        # Form submit button
        if st.form_submit_button('Save Changes'):
            # Update the stored data with edited values
            if 'basic_information' not in data:
                data['basic_information'] = {}
            data['basic_information'].update({
                '-_company_name': company_name,
                '-_company_type': company_type,
                '-_jurisdiction': jurisdiction
            })
            
            # Get company name for filename
            company_name = data['basic_information'].get('-_company_name', 'company')
            
            # Save JSON file
            json_path = save_json(data, company_name)
            
            st.success(f'Changes saved successfully! Data written to: {json_path}')

    # Debug information expander
    with st.expander("Debug Information", expanded=False):
        st.subheader("Raw LLM Response")
        st.code(st.session_state.debug_info['raw_response'], language='markdown')
        
        st.subheader("Parsed Sections")
        st.json(st.session_state.debug_info['parsed_sections'])
        
        if st.session_state.debug_info['skipped_lines']:
            st.subheader("Skipped Lines")
            st.json(st.session_state.debug_info['skipped_lines'])
        
        st.subheader("Structured Data")
        st.json(st.session_state.extracted_data)

    if st.button('Generate Wiki'):
        try:
            # Convert JSON to markdown
            markdown_content = json_to_markdown(st.session_state.extracted_data)
            
            # Get company name for filename
            company_name = st.session_state.extracted_data.get('basic_information', {}).get('-_company_name', 'company')
            
            # Save markdown file
            markdown_path = save_markdown(markdown_content, company_name)
            
            # Show preview of markdown
            st.subheader("Generated Wiki Content")
            st.markdown(markdown_content)
            
            # Show file location
            st.success(f'Wiki content generated and saved to: {markdown_path}')
            
            # Add info about PDF generation
            st.info('To generate PDF from command line, run:\n' +
                   f'`python utils/pdf_generator.py {markdown_path}`')
            
        except Exception as e:
            st.error(f'Error generating wiki content: {str(e)}')
