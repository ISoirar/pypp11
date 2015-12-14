template<class T>
class ref_ptr
{
};

template<class T>
class buffered_value
{
public:
    buffered_value() {}
    buffered_value(unsigned int size) {}
    buffered_value& operator = (const buffered_value& rhs) {}
};

class Referenced
{
public:
    Referenced() {}
    Referenced(const Referenced&) {}
protected:
    virtual ~Referenced() {}
};

class Object : public Referenced
{
public:
    Object() {}
    virtual const char* className() const = 0;

protected:
    virtual ~Object() {}
};

class Shader : public Object
{
public:

    virtual const char* className() const  { return "Shader"; }

    Shader() {}
    Shader(const char *source ) {}

protected:
    class PerContextShader : public Referenced
    {
        public:
            PerContextShader(const Shader* shader, unsigned int contextID) {}

        protected:
            ~PerContextShader() {}

        private:
            PerContextShader() {}
            PerContextShader(const PerContextShader&) {}
            PerContextShader& operator=(const PerContextShader&) {}
    };

protected:
    virtual ~Shader() {}

    PerContextShader* getPCS(unsigned int contextID) const {}

protected:
    mutable buffered_value< ref_ptr<PerContextShader> > _pcsList;
};
 
