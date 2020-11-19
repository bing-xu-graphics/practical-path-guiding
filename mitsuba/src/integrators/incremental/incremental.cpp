#include <mitsuba/render/scene.h>
MTS_NAMESPACE_BEGIN

class IncrementalIntegrator : public SamplingIntegrator {
public:
/*
//ensure that this class is recognized sas a native Mtsuba class.
this is necessary to get things like run-time type information , reference counting,
and serialization/unserialization support. 
*/
    MIS_DECLARE_CLASS() 


};

/**
 * MTS_IMPLEMENT_CLASS_S
 * The suffix S specifies that this is a serializable class, which means that this can be sent 
 * over the network or written to disk and later restored. 
 *  the name of this class(MyIntegrator), the fact that it is not an abstract class(false), 
 * and the name of its parent class(SamplingIntegrator)
 * 
 * MTS_EXPORT_PLUGIN
 * 
 */
MTS_IMPLEMENT_CLASS_S(IncrementalIntegrator, fasle, SamplingIntegrator)
MTS_EXPORT_PLUGIN(IncrementalIntegrator, "An incremental ingegrator for dynamic scenes");
MTS_NAMESPACE_END