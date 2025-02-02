"""
Enhanced NLP processor for intent recognition and entity extraction.
"""

import re
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple
import spacy
from textblob import TextBlob

class Intent(Enum):
    """Possible conversation intents."""
    FORMATION = auto()
    CONSULTATION = auto()
    INFORMATION = auto()
    CLARIFICATION = auto()
    COMPARISON = auto()
    COST = auto()
    TIMELINE = auto()
    REQUIREMENTS = auto()
    HELP = auto()

class EnhancedNLPProcessor:
    """Advanced NLP processor for LLC formation assistance."""
    
    def __init__(self):
        """Initialize the NLP processor."""
        try:
            # Load spaCy model
            self.nlp = spacy.load("en_core_web_sm")
            
            # Intent patterns
            self._intent_patterns = {
                Intent.FORMATION: {
                    'patterns': [
                        'how do i form', 'how to form', 'want to form', 'need to form',
                        'start an llc', 'create an llc', 'establish an llc', 'set up an llc',
                        'register an llc', 'incorporate', 'formation', 'begin'
                    ],
                    'context': ['llc', 'business', 'company', 'corporation']
                },
                Intent.CONSULTATION: {
                    'patterns': [
                        'help me with', 'need advice', 'guide me', 'assist me',
                        'recommend', 'suggestion', 'what should i', 'how should i'
                    ],
                    'context': ['expert', 'professional', 'advisor', 'consultant']
                },
                Intent.INFORMATION: {
                    'patterns': [
                        'tell me about', 'what is', 'how do', 'explain',
                        'information on', 'details about', 'learn about', 'understand'
                    ],
                    'context': ['process', 'steps', 'requirements', 'procedure']
                },
                Intent.CLARIFICATION: {
                    'patterns': [
                        'what do you mean', 'dont understand', "don't understand",
                        'confused about', 'unclear', 'clarify', 'explain again'
                    ],
                    'context': []
                },
                Intent.COMPARISON: {
                    'patterns': [
                        'compare', 'difference between', 'versus', 'vs',
                        'better option', 'advantages', 'disadvantages', 'which is better'
                    ],
                    'context': ['types', 'options', 'alternatives', 'choices']
                },
                Intent.COST: {
                    'patterns': [
                        'how much', 'cost to', 'price of', 'fee for',
                        'expenses', 'charges', 'pricing', 'payment'
                    ],
                    'context': ['filing', 'registration', 'maintenance', 'setup']
                },
                Intent.TIMELINE: {
                    'patterns': [
                        'how long', 'time to', 'duration of', 'timeline for',
                        'when can i', 'schedule for', 'process time', 'waiting period'
                    ],
                    'context': ['complete', 'finish', 'approval', 'formation']
                },
                Intent.REQUIREMENTS: {
                    'patterns': [
                        'what do i need', 'requirements for', 'necessary for',
                        'required to', 'must have', 'prerequisites', 'mandatory'
                    ],
                    'context': ['document', 'file', 'submit', 'form']
                },
                Intent.HELP: {
                    'patterns': [
                        'help', 'assist', 'support', 'guide', 'stuck with',
                        'having trouble', 'not sure how', 'confused about'
                    ],
                    'context': []
                }
            }
            
            # Entity patterns
            self._entity_patterns = {
                'state_codes': r'(AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)',
                'currency': r'\$\d+(?:,\d{3})*(?:\.\d{2})?',
                'percentage': r'\d+(?:\.\d+)?%',
                'date': r'\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{2}-\d{2}'
            }
        
        except Exception as e:
            raise Exception(f"Failed to initialize NLP processor: {str(e)}")
    
    def process_text(self, text: str) -> Tuple[Intent, float]:
        """
        Process text to determine intent and confidence.
        
        Args:
            text: Input text to process
            
        Returns:
            Tuple of (Intent, confidence score)
        """
        try:
            # Convert to lowercase for pattern matching
            text = text.lower()
            
            # Process with spaCy
            doc = self.nlp(text)
            
            # Calculate intent scores
            intent_scores = {}
            
            for intent, patterns in self._intent_patterns.items():
                # Base score from pattern matches
                pattern_score = 0
                for pattern in patterns['patterns']:
                    if pattern in text:
                        pattern_score += 1
                        # Boost score for exact matches
                        if pattern == text.strip():
                            pattern_score += 0.5
                
                # Context score
                context_score = sum(
                    1 for context in patterns['context']
                    if context in text
                )
                
                # Combine scores with weights
                total_score = (pattern_score * 0.7) + (context_score * 0.3)
                
                # Apply length penalty for very short queries
                if len(text.split()) < 3:
                    total_score *= 0.8
                
                if total_score > 0:
                    intent_scores[intent] = total_score
            
            # Get highest scoring intent
            if not intent_scores:
                return Intent.HELP, 0.0
            
            best_intent = max(intent_scores.items(), key=lambda x: x[1])
            confidence = min(best_intent[1] / max(len(doc), 1), 1.0)
            
            return best_intent[0], confidence
        
        except Exception as e:
            raise Exception(f"Error processing text: {str(e)}")
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extract named entities and custom patterns from text.
        
        Args:
            text: Input text to process
            
        Returns:
            Dictionary of entity types and their values
        """
        try:
            # Process with spaCy
            doc = self.nlp(text)
            
            # Initialize entities dictionary
            entities = {
                'states': [],
                'organizations': [],
                'money': [],
                'dates': [],
                'people': []
            }
            
            # Extract spaCy entities
            for ent in doc.ents:
                if ent.label_ == 'GPE' and re.match(self._entity_patterns['state_codes'], ent.text):
                    entities['states'].append(ent.text)
                elif ent.label_ == 'ORG':
                    entities['organizations'].append(ent.text)
                elif ent.label_ == 'MONEY':
                    entities['money'].append(ent.text)
                elif ent.label_ == 'DATE':
                    entities['dates'].append(ent.text)
                elif ent.label_ == 'PERSON':
                    entities['people'].append(ent.text)
            
            # Extract custom patterns
            text = text.upper()  # For state codes
            
            # Find state codes
            state_matches = re.finditer(self._entity_patterns['state_codes'], text)
            entities['states'].extend(match.group() for match in state_matches)
            
            # Find currency amounts
            money_matches = re.finditer(self._entity_patterns['currency'], text)
            entities['money'].extend(match.group() for match in money_matches)
            
            # Remove duplicates while preserving order
            for key in entities:
                entities[key] = list(dict.fromkeys(entities[key]))
            
            return entities
        
        except Exception as e:
            raise Exception(f"Error extracting entities: {str(e)}")
    
    def analyze_sentiment(self, text: str) -> float:
        """
        Analyze sentiment of text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Sentiment polarity score (-1 to 1)
        """
        try:
            blob = TextBlob(text)
            return blob.sentiment.polarity
        except Exception as e:
            raise Exception(f"Error analyzing sentiment: {str(e)}")
    
    def get_complexity(self, text: str) -> str:
        """
        Assess complexity of text.
        
        Args:
            text: Input text to assess
            
        Returns:
            Complexity level ('simple', 'moderate', or 'complex')
        """
        try:
            doc = self.nlp(text)
            
            # Count complexity indicators
            indicators = {
                'sentence_length': len(list(doc.sents)) > 2,
                'technical_terms': any(token.text.lower() in {
                    'compliance', 'regulation', 'requirement', 'jurisdiction',
                    'incorporation', 'dissolution', 'amendment'
                } for token in doc),
                'subordinate_clauses': any(token.dep_ == 'advcl' for token in doc),
                'questions': len([token for token in doc if token.text == '?']) > 1
            }
            
            complexity_score = sum(indicators.values())
            
            if complexity_score <= 1:
                return 'simple'
            elif complexity_score <= 2:
                return 'moderate'
            else:
                return 'complex'
        
        except Exception as e:
            raise Exception(f"Error assessing complexity: {str(e)}")
    
    def get_urgency(self, text: str) -> str:
        """
        Detect urgency level in text.
        
        Args:
            text: Input text to assess
            
        Returns:
            Urgency level ('low', 'medium', or 'high')
        """
        try:
            text = text.lower()
            
            urgent_terms = {
                'high': {'immediate', 'urgent', 'asap', 'emergency', 'critical'},
                'medium': {'soon', 'quickly', 'priority', 'important'},
                'low': {'whenever', 'flexible', 'no rush', 'take time'}
            }
            
            # Check for urgent terms
            for level, terms in urgent_terms.items():
                if any(term in text for term in terms):
                    return level
            
            return 'low'
        
        except Exception as e:
            raise Exception(f"Error detecting urgency: {str(e)}")
