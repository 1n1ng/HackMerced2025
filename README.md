# HackMerced2025

## Inspiration...

The Healthcare Finder project was inspired by a fundamental problem many people face: accessing healthcare resources when they need them most. During times of illness or emergency, people often struggle to determine which healthcare facilities are nearby and appropriate for their specific needs. This challenge is particularly acute for those who are new to an area, traveling, or simply unaware of local healthcare options.

I realized that while many mapping applications can show healthcare facilities, they lack the intelligent guidance needed to match a person's symptoms or health concerns with the most appropriate type of facility. This gap between information and actionable guidance is where our project found its purpose.

## What it does

Healthcare Finder combines location-based services with AI assistance to provide personalized healthcare recommendations. The application has two core functionalities:

1. **Location-based healthcare resource finder**: Users can enter their address to discover nearby hospitals, clinics, pharmacies, and other healthcare facilities.

2. **AI health assistant integration**: Powered by Google's Gemini AI, the assistant can:
   - Answer general healthcare questions
   - Provide basic guidance for common symptoms
   - Most importantly, analyze the user's health concerns alongside their location data to recommend specific nearby facilities that are best suited to address their needs

For example, if a user reports having a fever, the AI can suggest whether they should visit a nearby pharmacy for over-the-counter medication or seek care at an urgent care facility based on the severity of symptoms and available local resources.

## How we built it

The application was built using the following technologies and approaches:

- **Backend**: Flask web framework in Python
- **Frontend**: HTML, CSS, and JavaScript for a responsive, user-friendly interface
- **Geolocation services**: 
  - OpenStreetMap's Nominatim API for geocoding addresses
  - Overpass API to identify healthcare facilities near a location
- **AI integration**: Google's Gemini API for natural language understanding and healthcare guidance
- **Data persistence**: Flask sessions to maintain context between user interactions
- **Cross-functionality**: Custom integration between the AI assistant and location services

The development process involved creating a foundation for location-based searches, implementing the AI assistant functionality, and then building the crucial bridge between these two systems to enable location-aware AI recommendations.

## Challenges we faced

Several significant challenges emerged during development:

1. **Maintaining context across different functions**: Ensuring the AI assistant remembers previous interactions while incorporating new location data required careful session management.

2. **API rate limiting and reliability**: The geolocation APIs occasionally returned incomplete data or imposed request limits, requiring robust error handling.

3. **Prompt engineering**: Crafting effective prompts for the Gemini AI to generate concise, helpful, and medically responsible recommendations without crossing into providing medical advice was delicate work.

4. **Response formatting**: Initially, the AI responses included HTML tags that appeared in the interface. Resolving this required modifications to both the prompt engineering and frontend rendering.

5. **State persistence**: Balancing the need to maintain conversation state within a session while ensuring fresh starts for new users required careful implementation of session management.

## What we learned

This project provided valuable insights and learning opportunities:

- **AI prompt design is crucial**: The quality and usefulness of AI responses depend heavily on well-crafted prompts that provide clear constraints and expectations.

- **Session management complexity**: Web applications that maintain state across different user flows require careful planning to handle all possible interaction paths.

- **The power of combining technologies**: Individually, mapping services and AI assistants are useful, but their combination creates a significantly more valuable service than either alone.

- **Responsible AI implementation**: When dealing with healthcare information, it's essential to frame AI responses responsibly, with appropriate disclaimers and guidance toward professional medical care when needed.

- **User experience considerations**: Technical functionality must be balanced with an intuitive interface that guides users naturally between different application features.

## What's next for our project

The Healthcare Finder project has significant potential for expansion:

- **Enhanced AI capabilities**: Training the model with more specific healthcare knowledge to provide more tailored recommendations.

- **Mobile application**: Developing a native mobile app with GPS integration to further streamline the location aspect.

- **Integration with healthcare providers**: Partnering with healthcare networks to include appointment scheduling directly within the application.

- **Expanded resource database**: Including more specialized healthcare facilities, community resources, and support services.

- **Multilingual support**: Adding multiple languages to make the service accessible to diverse communities.

- **Accessibility features**: Implementing voice interaction for users who may have difficulty with text input, especially when unwell.

The ultimate vision is to create a comprehensive healthcare navigation tool that removes barriers to appropriate care and empowers users to make informed healthcare decisions based on their specific needs and local resources.
