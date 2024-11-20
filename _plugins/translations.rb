module Jekyll
    class DummyTranslator
      def self.translate(input)
        input
      end
    end
  end
  
  Liquid::Template.register_filter(Jekyll::DummyTranslator)
  